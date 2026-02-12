from PyPDF2 import PdfReader, PdfWriter, PdfMerger


class PdfTools:
    """
    A utility class for performing common PDF operations.

    Provides functionality for reading PDF metadata, merging PDFs,
    extracting text, splitting pages, rotating pages, deleting pages,
    encrypting/decrypting PDFs, applying watermarks, and previewing pages.
    """

    def __init__(self, input_file):
        """
        Initialize the PdfTools object with a PDF file.

        :param input_file: Path to the input PDF file.
        :type input_file: str
        """
        self.reader = PdfReader(input_file)

    def info(self):
        """
        Retrieve basic information about the PDF.

        :return: A formatted string containing page count, encryption
                 status, and metadata.
        :rtype: str
        """
        if self.reader.is_encrypted:
            return """
pages     : Unavailable (file is encrypted)
encrypted : True
metadata  : Unavailable (file must be decrypted first)
"""
        
        metadata = {k: str(v) for k, v in (self.reader.metadata or {}).items()} or "None"
        return f"""
pages     : {len(self.reader.pages)}
encrypted : False
metadata  : {metadata}
"""

    @staticmethod
    def merge_pdfs(input_file_list, output_file):
        """
        Merge multiple PDF files into a single PDF.

        :param input_file_list: List of input PDF file paths.
        :type input_file_list: list[str]
        :param output_file: Output file path for the merged PDF.
        :type output_file: str
        :return: Status message indicating success.
        :rtype: str
        """
        merger = PdfMerger()
        
        for file in input_file_list:
            merger.append(file)
        
        merger.write(output_file)
        merger.close()
        return f"PDFs merged → {output_file}"

    def extract_text(self, page_num=None, output_file=None):
        """
        Extract text from the PDF.

        :param page_num: Page number to extract text from (1-based).
                         If None, text is extracted from all pages.
        :type page_num: int | None
        :param output_file: Optional file path to save extracted text.
        :type output_file: str | None
        :return: Extracted text or confirmation message if saved.
        :rtype: str
        :raises ValueError: If an invalid page number is provided.
        """
        if page_num is not None:
            if not (1 <= page_num <= len(self.reader.pages)):
                raise ValueError("Invalid page number") 
            text = self.reader.pages[page_num - 1].extract_text() or ""
        else:
            text = "".join(page.extract_text() or "" for page in self.reader.pages)
        
        if output_file:
            with open(output_file, 'w', encoding="utf-8") as f:
                f.write(text or "")
            return f"Text saved to {output_file}"
        return text

    def split(self, pages_list, output_file):
        """
        Create a new PDF using selected pages from the original PDF.

        :param pages_list: List of page numbers to include (1-based).
        :type pages_list: list[int]
        :param output_file: Output file path for the new PDF.
        :type output_file: str
        :return: Status message indicating success.
        :rtype: str
        :raises ValueError: If the page list is empty or contains invalid pages.
        """
        if len(pages_list) == 0:
            raise ValueError("Page_list is empty")

        writer = PdfWriter()

        for page in pages_list:
            if not (1 <= page <= len(self.reader.pages)):
                raise ValueError("Invalid page number")
            writer.add_page(self.reader.pages[page - 1])
        
        with open(output_file, 'wb') as f:
            writer.write(f)
        
        return f"PDF split successfully → {output_file}"

    def rotate_page(self, page_num, angle, output_file):
        """
        Rotate a specific page of the PDF.

        :param page_num: Page number to rotate (1-based).
        :type page_num: int
        :param angle: Angle of rotation in degrees.
        :type angle: int
        :param output_file: Output file path for the rotated PDF.
        :type output_file: str
        :return: Status message indicating success.
        :rtype: str
        :raises ValueError: If an invalid page number is provided.
        """
        if not (1 <= page_num <= len(self.reader.pages)):
            raise ValueError("Invalid page number")
        writer = PdfWriter()
        page_num -= 1
        page = self.reader.pages[page_num]
        page.rotate(angle)

        for p in range(len(self.reader.pages)):
            if p == page_num:
                writer.add_page(page)
            else:
                writer.add_page(self.reader.pages[p])
        
        with open(output_file, "wb") as f:
            writer.write(f)
        
        return f"Page {page_num+1} rotated by {angle}° → {output_file}"

    def delete_pages(self, page_num, output_file):
        """
        Delete a specific page from the PDF.

        :param page_num: Page number to delete (1-based).
        :type page_num: int
        :param output_file: Output file path for the new PDF.
        :type output_file: str
        :return: Status message indicating success.
        :rtype: str
        :raises ValueError: If an invalid page number is provided.
        """
        if not (1 <= page_num <= len(self.reader.pages)):
            raise ValueError("Invalid page number")
        writer = PdfWriter()
        page_num -= 1

        for p in range(len(self.reader.pages)):
            if p != page_num:
                writer.add_page(self.reader.pages[p])
        
        with open(output_file, "wb") as f:
            writer.write(f)
        
        return f"Page {page_num+1} deleted → {output_file}"

    def encrypt_file(self, output_file, user_pwd, owner_pwd=None):
        """
        Encrypt the PDF file with a password.

        :param output_file: Output file path for the encrypted PDF.
        :type output_file: str
        :param user_pwd: User password for encryption.
        :type user_pwd: str
        :param owner_pwd: Optional owner password.
        :type owner_pwd: str | None
        :return: Status message indicating success.
        :rtype: str
        :raises ValueError: If the PDF is already encrypted or password is missing.
        """
        if not self.reader.is_encrypted:
            if user_pwd is None:
                raise ValueError("User password cannot be empty")

            writer = PdfWriter()
            for page in self.reader.pages:
                writer.add_page(page)
            
            writer.encrypt(user_password=user_pwd, owner_password=owner_pwd)

            with open(output_file, "wb") as f:
                writer.write(f)

            self.reader = PdfReader(output_file)

            return f"PDF encrypted → {output_file}: password → {user_pwd}"
        else:
            raise ValueError("PDF is already encrypted")

    def decrypt_file(self, password, output_file):
        """
        Decrypt an encrypted PDF file.

        :param password: Password for the encrypted PDF.
        :type password: str
        :param output_file: Output file path for the decrypted PDF.
        :type output_file: str
        :return: Status message indicating success.
        :rtype: str
        :raises ValueError: If the password is incorrect.
        """
        writer = PdfWriter()

        if self.reader.is_encrypted:
            if self.reader.decrypt(password) == 0:
                raise ValueError("Invalid password")
        
        for page in self.reader.pages:
            writer.add_page(page)
        
        with open(output_file, "wb") as f:
            writer.write(f)

        self.reader = PdfReader(output_file)

        return f"PDF decrypted → {output_file}"

    def watermark_apply(self, watermark_file_path, output_file):
        """
        Apply a watermark PDF to every page of the PDF.

        :param watermark_file_path: Path to the watermark PDF file.
        :type watermark_file_path: str
        :param output_file: Output file path for the watermarked PDF.
        :type output_file: str
        :return: Status message indicating success.
        :rtype: str
        """
        watermark_reader = PdfReader(watermark_file_path)
        watermark_page = watermark_reader.pages[0]

        output_writer = PdfWriter()
        for page in self.reader.pages:
            page.merge_page(watermark_page)
            output_writer.add_page(page)
        
        with open(output_file , "wb") as f:
            output_writer.write(f)
        
        return f"Watermark applied → {output_file}"

    def list_pages(self, snippet_length=200, keyword=None):
        """
        Generate a short text preview for each page of the PDF.

        :param snippet_length: Number of characters to include in the preview.
        :type snippet_length: int
        :param keyword: Optional keyword to highlight in the text.
        :type keyword: str | None
        :return: Dictionary mapping page numbers to text snippets.
        :rtype: dict[int, str]
        :raises ValueError: If the PDF is encrypted.
        """
        if self.reader.is_encrypted:
            raise ValueError("PDF is encrypted — please decrypt before listing page text.")
        
        page_summary = {}
        for i, page in enumerate(self.reader.pages, start=1):
            text = page.extract_text() or ""
            snippet = text[:snippet_length].replace("\n", " ")
            if keyword and keyword.lower() in text.lower():
                snippet = snippet.replace(keyword, f"[{keyword}]")
            if snippet.strip():
                page_summary[i] = snippet
        return page_summary
