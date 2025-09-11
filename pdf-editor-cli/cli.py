from pdf_tools import PdfTools
import os
import time
import random
import string

def clear_screen():

    if os.name == 'nt':
        os.system("cls")

    else:
        os.system("clear")

def get_default_output_dir():
    """Generates a default directory to store output"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    default_dir = os.path.join(base_dir, "output")
    os.makedirs(default_dir, exist_ok=True)
    return default_dir

def output_file_location(format='pdf'):
    """Confirms the name and location of the output"""
    while True:
        output_name = input("What would you like to name your file? (no extension, or type 'exit' to abort operation)\n=> ").strip()
        print("\n")

        if output_name == "exit":
            return None
        
        if output_name == "":
            print("❌ File name cannot be empty")
            print("\n")
            continue
        break

    output_dir = input(
    "Please provide a directory path for custom save location "
    "or press enter key to save in default save location\n=> ")

    if output_dir == "":
        output_dir = get_default_output_dir()
    else:
        if not os.path.isdir(output_dir):
            print("❌ Directory not found. Using default save location instead.")
            print("\n")   
            output_dir = get_default_output_dir()
    
    output_file = os.path.join(output_dir, f"{output_name}.{format}")
    
    if os.path.exists(output_file):
        while True:
            confirmation = input("⚠️ File already exists. Would you like to overwrite it? (y/n)\n=> ").strip().lower()
            print("\n")
            if confirmation in ['y','n']:
                break
            print("Please enter either 'y' or 'n'")
            print("\n")
            
        if confirmation == "n":
            while True:
                new_name = input("Enter a new name (no extension, or type 'exit' to abort operation)\n=> ").strip()
                print("\n")

                if new_name == "":
                    print("❌ File name cannot be empty")
                    print("\n")
                    continue
                new_file = os.path.join(output_dir, f"{new_name}.{format}")
                if os.path.exists(new_file):
                    print("❌ That name already exists too, please choose another.")
                    print("\n")
                    continue
                output_file = new_file
                break
        
    return output_file

def random_password_generator():
    """Generates a random password with user-selected options.
       Ensures at least one character from each chosen type is included."""

    def ask_choice(prompt):
        while True:
            choice = input(f"{prompt} (y/n): ").lower().strip()
            if choice in ["y", "n"]:
                return choice == "y"
            print("❌ Invalid input! Please enter 'y' or 'n'.")

    # Get password length
    while True:
        try:
            length = int(input("Enter length of password to generate (≥ 4):\n=> "))
            if length < 4:
                print("❌ Please enter a value ≥ 4 for a strong password.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a positive integer.")
    # Character sets
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
        print("❌ You must select at least one character type!")
        return None

    # Ensure at least one character from each chosen type
    password_chars = [random.choice(opt) for opt in options]

    # Fill the rest randomly from all selected pools
    all_chars = "".join(options)
    password_chars += random.choices(all_chars, k=length - len(password_chars))

    # Shuffle so guaranteed chars aren't always at the start
    random.shuffle(password_chars)

    return "".join(password_chars)

def pause_and_continue(func):
    def wrapper(*args, **kwargs):
       result = func(*args, **kwargs)
       input("\nPress Enter to go back to the main menu...")
       clear_screen()
       return result

    return wrapper

@pause_and_continue
def op_check_info(pdf: PdfTools):
    print("📑 Checking PDF info...")
    time.sleep(0.5)
    print(pdf.info())

@pause_and_continue
def op_extract_text(pdf: PdfTools):
    page_num = input(
        "Enter page number to extract text from "
        "(or press Enter for whole PDF):\n=> ").strip()
    
    if page_num == "":
        page_num = None
    else:
        try:
            page_num = int(page_num)
        except ValueError:
            print("❌ Invalid input.")
            pause_and_continue()
            return
        
    while True:
        usr_choice = input("To save text as a text file enter 'y' or enter 'n' to view on terminal\n=> ").strip().lower()
        if usr_choice in ['y','n']:
            break
        print("Invalid input! Please enter either 'y' or 'n'.")

    if usr_choice == 'y':
        output_file = output_file_location(format="txt")
        print("Extracting text...")
        time.sleep(0.5)
        try:
            pdf.extract_text(page_num, output_file)
            print("Saving text...")
            time.sleep(0.5)
        except ValueError as e:
            print(f"❌ Error: {e}")

    else:        
        try:
            text = pdf.extract_text(page_num)
            while True:
                preview = input("Do you want to preview first 100 chars? (y/n): ").strip().lower()
                if preview in ['y','n']:
                    break
                print("Invalid input! Please enter either 'y' or 'n'.")

            print("\n✅ Extracted text:\n")
            if preview == 'y':
                print(text[:100] + ("..." if len(text) > 1000 else ""))
            else:
                print(text)
        except ValueError as e:
            print(f"❌ Error: {e}")

@pause_and_continue
def op_split_pdf(pdf: PdfTools):
    raw_input = input("Enter the page numbers (separated by ',') to split\n=> ").strip()
    try:
        page_num_list = [int(p.strip()) for p in raw_input.split(',')]
    except ValueError:
        print("❌ Error: All page numbers must be integers.")
        return

    output_file = output_file_location()
    print("Splitting PDF...")
    time.sleep(0.5)
    try:
        print("✅ " + pdf.split(page_num_list, output_file))
    except ValueError as e:
        print(f"❌ Error: {e}")

@pause_and_continue
def op_rotate_page(pdf :PdfTools):
        try:
            page_num = int(input("Enter the number of the page to rotate").strip())
        except ValueError:
            print("❌ Error: Invalid input.")
            return

        try:
            angle_to_rotate = int(input("Enter the angle of rotation\n=> ").strip())
        except ValueError:
            print("❌ Error: Invalid input.")
            return

        output_file = output_file_location()              
        try:
            print("✅ "+ pdf.rotate_page(page_num, angle_to_rotate,output_file))
        except ValueError as e:
            print(f"❌ Error: {e}")

@pause_and_continue
def op_delete_page(pdf: PdfTools):
    try:
        page_num = int(input("Enter the page number of the page to delete\n=> ").strip())
    except ValueError:
        print("❌ Error: Invalid input.")
        return
        
    output_file = output_file_location()
    print("Deleting page...")
    time.sleep(0.5)
    try:
        print("✅ "+ pdf.delete_pages(page_num,output_file))
    except ValueError as e:
        print(f"❌ Error: {e}")

@pause_and_continue
def op_encrypt_pdf(pdf: PdfTools):
    while True:
        custom_pwd_choice = input("To set a custom password enter 'y' or 'n' for random password\n=> ").lower()
        if custom_pwd_choice in ["y","n"]:
            break
        print("Invalid input! Please enter either 'y' or 'n'.")

    if custom_pwd_choice == 'y':
        while True:
            set_cust_pwd = input("Set password: ")
            confirm_cust_pwd = input("Confirm password: ")
            if set_cust_pwd == confirm_cust_pwd:
                break
            print("Password does not match, try agian.")
        usr_pwd = set_cust_pwd
        del confirm_cust_pwd
    else:
        usr_pwd = random_password_generator()
    
    output_file = output_file_location()
    print("Encrypting PDF...")
    time.sleep(0.5)
    try:
        print("✅ "+ pdf.encrypt_file(output_file,user_pwd=usr_pwd))
    except ValueError as e:
        print(f"❌ Error: {e}")

@pause_and_continue
def op_decrypt_pdf(pdf: PdfTools):
    password = input("Provide the password of the file to start decrypting: ")
    output_file = output_file_location()
    print("Decrypting PDF...")
    time.sleep(0.5)
    try:
        print("✅ "+ pdf.decrypt_file(password, output_file))
    except ValueError as e:
        print(f"❌ Error: {e}")
                    
@pause_and_continue
def op_watermark_pdf(pdf: PdfTools):
    watermark_file_path = input("Provide the path of the watermark file"
                            "(ensure that the file is in PDF format)\n=> ")
    if not os.path.isfile(watermark_file_path) or not watermark_file_path.lower().endswith(".pdf"):
        print("❌ Error: File does not exist or is not a PDF format")
        print("\n")
        return
    
    print("Applying watermark...")
    output_file = output_file_location()
    print("✅ " + pdf.watermark_apply(watermark_file_path, output_file))

@pause_and_continue
def op_list_pages(pdf: PdfTools):
    try:
        summaries = pdf.list_pages()
        for page, snippet in summaries.items():
            print(f"📄 Page {page}: {snippet}")
    except ValueError as e:
        print(f"❌ Error: {e}")

clear_screen()
print(("*"*15 + "PDF EDITOR" + "*"*15).center(50))
print("="*50)
time.sleep(0.5)

input_file_path = input(
    "Please enter the file path of the PDF to start editing "
    "or press enter to merge multiple PDFs\n=> ").strip(" \"")
time.sleep(0.5)

if input_file_path == "":
    raw_input = input("Enter the file path of all the PDFs to merge, separated by ','\n=> ").strip()
    print("\n")
    if raw_input:
        input_files = [f.strip(" '\"") for f in raw_input.split(",") if f.strip(" '\"")]
    else:
        print("No input provided.")
        print("\n")
    
    output_file = output_file_location()
    print("✅ " + PdfTools.merge_pdfs(input_files, output_file))
    
if not os.path.isfile(input_file_path) or not input_file_path.lower().endswith(".pdf"):
    print("❌ Error: File does not exist or is not a PDF format")
    print("\n")
else:
    pdf = PdfTools(input_file_path)
    while True:
        try:
            operation_choice = int(input("""
Please enter the serial no. of the below operations to perform that operation:
    1  - Check info of the PDF
    2  - Extract text from the PDF
    3  - Make a new PDF with only specific pages from old PDF
    4  - Rotate a certain page of the PDF
    5  - Delete a certain page from the PDF
    6  - Encrypt (put password and lock) the PDF
    7  - Decrypt (remove password and unlock) the PDF
    8  - Put watermark on every page of the PDF
    9  - View first 200 letters of each page of the PDF
    10  - Quit
=> """).strip())

            if operation_choice not in range(1,11):
                print("\n")
                print("⚠️ Invalid input, please enter a number between 1–10.")
                continue

        except ValueError:
            print("\n")
            print("⚠️ Invalid input, please enter a number between 1–10.")
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

