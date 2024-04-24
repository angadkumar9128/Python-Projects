elif choice == 3:
            input_pdf_path = input("Enter the input PDF file path: ")
            pdf_to_img_pypdf2(input_pdf_path)
            print("Conversion successful!")