from pdf_tools import PdfTools
from functools import wraps
import os
import time
import random
import string


def clear_screen():
    """
    Clear the terminal screen.

    Uses 'cls' on Windows and 'clear' on Unix-based systems.
    """
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def get_default_output_dir():
    """
    Generate and return the default output directory path.

    Creates an 'output' directory relative to the script location
    if it does not already exist.

    :return: Path to the default output directory.
    :rtype: str
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_dir = os.path.join(base_dir, "output")
    os.makedirs(default_dir, exist_ok=True)
    return default_dir


def output_file_location(format='pdf'):
    """
    Prompt the user for an output file name and save location.

    Handles directory validation and overwrite confirmation.

    :param format: File extension to use for the output file.
    :type format: str
    :return: Full path to the output file, or None if aborted.
    :rtype: str | None
    """
    while True:
        output_name = input(
            "What would you like to name your file? "
            "(no extension, or type 'exit' to abort operation)\n=> "
        ).strip()

        if output_name == "exit":
            return None

        if not output_name:
            print("❌ File name cannot be empty\n")
            continue
        break

    output_dir = input(
        "Provide a directory path for custom save location "
        "or press Enter to use the default location\n=> "
    ).strip()

    if not output_dir:
        output_dir = get_default_output_dir()
    elif not os.path.isdir(output_dir):
        print("❌ Directory not found. Using default save location.\n")
        output_dir = get_default_output_dir()

    output_file = os.path.join(output_dir, f"{output_name}.{format}")

    if os.path.exists(output_file):
        while True:
            confirm = input(
                "⚠️ File exists. Overwrite? (y/n)\n=> "
            ).strip().lower()
            if confirm in ('y', 'n'):
                break
            print("Please enter 'y' or 'n'\n")

        if confirm == 'n':
            while True:
                new_name = input(
                    "Enter a new name (no extension)\n=> "
                ).strip()
                if not new_name:
                    print("❌ File name cannot be empty\n")
                    continue
                new_file = os.path.join(output_dir, f"{new_name}.{format}")
                if os.path.exists(new_file):
                    print("❌ That name already exists\n")
                    continue
                output_file = new_file
                break

    return output_file


def random_password_generator():
    """
    Generate a random password based on user-selected options.

    Ensures at least one character from each selected character
    type is included.

    :return: Generated password.
    :rtype: str | None
    """

    def ask_choice(prompt):
        """
        Prompt the user with a yes/no question.

        :param prompt: Question to display to the user.
        :type prompt: str
        :return: True if 'y', False if 'n'.
        :rtype: bool
        """
        while True:
            choice = input(f"{prompt} (y/n): ").strip().lower()
            if choice in ('y', 'n'):
                return choice == 'y'
            print("❌ Invalid input! Please enter 'y' or 'n'.")

    while True:
        try:
            length = int(input("Enter password length (≥ 4):\n=> "))
            if length < 4:
                print("❌ Password must be at least 4 characters.")
                continue
            break
        except ValueError:
            print("❌ Enter a valid integer.")

    options = []
    if ask_choice("Include uppercase letters"):
        options.append(string.ascii_uppercase)
    if ask_choice("Include lowercase letters"):
        options.append(string.ascii_lowercase)
    if ask_choice("Include numbers"):
        options.append(string.digits)
    if ask_choice("Include symbols"):
        options.append(string.punctuation)

    if not options:
        print("❌ At least one character type must be selected.")
        return None

    password_chars = [random.choice(opt) for opt in options]
    all_chars = "".join(options)
    password_chars += random.choices(all_chars, k=length - len(password_chars))
    random.shuffle(password_chars)

    return "".join(password_chars)


def pause_and_continue(func):
    """
    Decorator that pauses execution after a function runs,
    waits for user input, then clears the screen.

    :param func: Function to wrap.
    :type func: callable
    :return: Wrapped function.
    :rtype: callable
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        input("\nPress Enter to return to the main menu...")
        clear_screen()
        return result

    return wrapper


@pause_and_continue
def op_check_info(pdf: PdfTools):
    """
    Display metadata information about a PDF file.

    :param pdf: PdfTools instance representing the PDF.
    :type pdf: PdfTools
    """
    print("📑 Checking PDF info...")
    time.sleep(0.5)
    print(pdf.info())


@pause_and_continue
def op_extract_text(pdf: PdfTools):
    """
    Extract text from a PDF file and display it or save it to a text file.

    The user may choose a specific page or extract from the entire PDF.

    :param pdf: PdfTools instance representing the PDF.
    :type pdf: PdfTools
    """
    page_num = input(
        "Enter page number (or press Enter for full PDF):\n=> "
    ).strip()

    if page_num == "":
        page_num = None
    else:
        try:
            page_num = int(page_num)
        except ValueError:
            print("❌ Invalid page number.")
            return

    while True:
        choice = input(
            "Save as text file? (y = save / n = display)\n=> "
        ).strip().lower()
        if choice in ('y', 'n'):
            break
        print("Invalid input.")

    try:
        if choice == 'y':
            output_file = output_file_location(format="txt")
            print("Extracting text...")
            time.sleep(0.5)
            pdf.extract_text(page_num, output_file)
            print("✅ Text saved successfully.")
        else:
            text = pdf.extract_text(page_num)
            print("\n✅ Extracted text:\n")
            print(text)
    except ValueError as e:
        print(f"❌ Error: {e}")


@pause_and_continue
def op_split_pdf(pdf: PdfTools):
    """
    Create a new PDF using selected pages from the original PDF.

    :param pdf: PdfTools instance representing the PDF.
    :type pdf: PdfTools
    """
    raw = input("Enter page numbers separated by commas:\n=> ")
    try:
        pages = [int(p.strip()) for p in raw.split(',')]
    except ValueError:
        print("❌ Invalid page numbers.")
        return

    output_file = output_file_location()
    print("Splitting PDF...")
    time.sleep(0.5)
    try:
        print("✅ " + pdf.split(pages, output_file))
    except ValueError as e:
        print(f"❌ Error: {e}")


@pause_and_continue
def op_rotate_page(pdf: PdfTools):
    """
    Rotate a specific page in the PDF.

    :param pdf: PdfTools instance representing the PDF.
    :type pdf: PdfTools
    """
    try:
        page = int(input("Enter page number:\n=> "))
        angle = int(input("Enter rotation angle:\n=> "))
    except ValueError:
        print("❌ Invalid input.")
        return

    output_file = output_file_location()
    try:
        print("✅ " + pdf.rotate_page(page, angle, output_file))
    except ValueError as e:
        print(f"❌ Error: {e}")


@pause_and_continue
def op_delete_page(pdf: PdfTools):
    """
    Delete a specific page from the PDF.

    :param pdf: PdfTools instance representing the PDF.
    :type pdf: PdfTools
    """
    try:
        page = int(input("Enter page number to delete:\n=> "))
    except ValueError:
        print("❌ Invalid input.")
        return

    output_file = output_file_location()
    try:
        print("✅ " + pdf.delete_pages(page, output_file))
    except ValueError as e:
        print(f"❌ Error: {e}")


@pause_and_continue
def op_encrypt_pdf(pdf: PdfTools):
    """
    Encrypt a PDF using a user-defined or randomly generated password.

    :param pdf: PdfTools instance representing the PDF.
    :type pdf: PdfTools
    """
    while True:
        choice = input("Use custom password? (y/n)\n=> ").lower()
        if choice in ('y', 'n'):
            break

    if choice == 'y':
        while True:
            pwd = input("Set password: ")
            confirm = input("Confirm password: ")
            if pwd == confirm:
                break
            print("Passwords do not match.")
    else:
        pwd = random_password_generator()

    output_file = output_file_location()
    try:
        print("✅ " + pdf.encrypt_file(output_file, user_pwd=pwd))
    except ValueError as e:
        print(f"❌ Error: {e}")


@pause_and_continue
def op_decrypt_pdf(pdf: PdfTools):
    """
    Decrypt a password-protected PDF.

    :param pdf: PdfTools instance representing the PDF.
    :type pdf: PdfTools
    """
    pwd = input("Enter PDF password:\n=> ")
    output_file = output_file_location()
    try:
        print("✅ " + pdf.decrypt_file(pwd, output_file))
    except ValueError as e:
        print(f"❌ Error: {e}")


@pause_and_continue
def op_watermark_pdf(pdf: PdfTools):
    """
    Apply a watermark PDF to every page of the source PDF.

    :param pdf: PdfTools instance representing the PDF.
    :type pdf: PdfTools
    """
    watermark = input("Enter watermark PDF path:\n=> ")
    if not os.path.isfile(watermark) or not watermark.lower().endswith(".pdf"):
        print("❌ Invalid watermark file.")
        return

    output_file = output_file_location()
    print("✅ " + pdf.watermark_apply(watermark, output_file))


@pause_and_continue
def op_list_pages(pdf: PdfTools):
    """
    Display a short text preview of each page in the PDF.

    :param pdf: PdfTools instance representing the PDF.
    :type pdf: PdfTools
    """
    try:
        summaries = pdf.list_pages()
        for page, snippet in summaries.items():
            print(f"📄 Page {page}: {snippet}")
    except ValueError as e:
        print(f"❌ Error: {e}")

clear_screen()
print(("*" * 15 + " PDF EDITOR " + "*" * 15).center(50))
print("=" * 50)
time.sleep(0.5)

input_file_path = input(
    "Enter the file path of the PDF to start editing\n"
    "or press Enter to merge multiple PDFs\n=> "
).strip(" \"")
time.sleep(0.5)

if input_file_path == "":
    raw_input_files = input(
        "Enter the file paths of PDFs to merge (comma-separated):\n=> "
    ).strip()

    if not raw_input_files:
        print("❌ No input provided.")
    else:
        input_files = [
            f.strip(" '\"") for f in raw_input_files.split(",") if f.strip(" '\"")
        ]
        output_file = output_file_location()
        print("✅ " + PdfTools.merge_pdfs(input_files, output_file))

else:
    if not os.path.isfile(input_file_path) or not input_file_path.lower().endswith(".pdf"):
        print("❌ Error: File does not exist or is not a PDF file.")
    else:
        pdf = PdfTools(input_file_path)

        while True:
            try:
                operation_choice = int(input("""
Please choose an operation:

1  - Check PDF info
2  - Extract text from PDF
3  - Split PDF (select pages)
4  - Rotate a page
5  - Delete a page
6  - Encrypt PDF
7  - Decrypt PDF
8  - Apply watermark
9  - Preview pages
10 - Quit

=> """).strip())

                if operation_choice not in range(1, 11):
                    print("⚠️ Please enter a number between 1 and 10.")
                    continue

            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")
                continue

            match operation_choice:
                case 1:
                    op_check_info(pdf)
                case 2:
                    op_extract_text(pdf)
                case 3:
                    op_split_pdf(pdf)
                case 4:
                    op_rotate_page(pdf)
                case 5:
                    op_delete_page(pdf)
                case 6:
                    op_encrypt_pdf(pdf)
                case 7:
                    op_decrypt_pdf(pdf)
                case 8:
                    op_watermark_pdf(pdf)
                case 9:
                    op_list_pages(pdf)
                case 10:
                    print("👋 Exiting program.")
                    break
