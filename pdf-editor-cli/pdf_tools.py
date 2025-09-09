from PyPDF2 import PdfReader, PdfWriter, PdfMerger


class PdfTools:

    def __init__(self, input_file):
        self.reader = PdfReader(input_file)

    def info(self):
        if self.reader.is_encrypted:
            return """
pages     : Unavailable (file is encrypted)
encrypted : True
metadata  : Unavailable (file must be decrypted first)
"""
        
        # Safe to read once not encrypted
        metadata = {k: str(v) for k, v in (self.reader.metadata or {}).items()} or "None"
        return f"""
pages     : {len(self.reader.pages)}
encrypted : False
metadata  : {metadata}
"""
    
    @staticmethod
    def merge_pdfs(input_file_list, output_file):
        merger = PdfMerger()
        
        for file in input_file_list:
            merger.append(file)
        
        merger.write(output_file)
        merger.close()
        return f"PDFs merged → {output_file}"

    def extract_text(self, page_num=None, output_file=None):
        if page_num is not None :
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
        if not (1 <= page_num <= len(self.reader.pages)):
            raise ValueError("Invalid page number")
        writer = PdfWriter()
        page_num -= 1
        page = self.reader.pages[page_num]
        page.rotate_counter_clockwise(angle)

        for p in range(len(self.reader.pages)):
            if p == page_num:
                writer.add_page(page)
            else:
                writer.add_page(self.reader.pages[p])
        
        with open(output_file, "wb") as f:
            writer.write(f)
        
        return f"Page {page_num+1} rotated by {angle}° → {output_file}"
        
        

    def delete_pages(self, page_num, output_file):
        if not (1 <= page_num <= len(self.reader.pages)):
            raise ValueError("Invalid page number")
        writer = PdfWriter()
        page_num -= 1

        for p in range(len(self.reader.pages)):
            if p != page_num :
                writer.add_page(self.reader.pages[p])
        
        with open(output_file, "wb") as f:
            writer.write(f)
        
        return f"Page {page_num+1} deleted → {output_file}"

    def encrypt_file(self, output_file, user_pwd, owner_pwd=None):
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


    def decrypt_file(self, password, output_file):
        writer = PdfWriter()

        if self.reader.is_encrypted:
            if self.reader.decrypt(password) == 0:
                raise ValueError("Invalid password")
        
        for page in self.reader.pages:
            writer.add_page(page)
        
        with open(output_file, "wb") as f:
            writer.write(f)

        # 🔄 Refresh the reader to point to the new decrypted file
        self.reader = PdfReader(output_file)

        return f"PDF decrypted → {output_file}"

    def watermark_apply(self, watermark_file_path, output_file):
        watermark_reader = PdfReader(watermark_file_path)
        watermark_page = watermark_reader.pages[0]

        output_writer = PdfWriter()
        for page in self.reader.pages:
            page.merge_page(watermark_page)
            output_writer.add_page(page)
        
        with open(output_file , "wb") as f:
            output_writer.write(f)
        
        return f"Watermark applied → {output_file}"
    

    def list_pages(self, snippet_length=100, keyword=None):
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


    # def exract_images(input_file, page_num, output_file):
        
    #     reader = PdfReader(input_file)
    #     image_page = reader.pages[page_num]
    #     extracted_image = image_page
        

    # def compress_size():
    #     pass
