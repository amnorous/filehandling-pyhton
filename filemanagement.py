def main():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
        return

    except PermissionError:
        print(f"❌ Error: Permission denied when trying to read '{input_filename}'.")
        return

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return

    modified_content = content.upper()

    output_filename = "modified_" + input_filename
    try:
        with open(output_filename, "w") as file:
            file.write(modified_content)
        print(f"✅ Modified file saved as '{output_filename}'.")
    except Exception as e:
        print(f"❌ Could not write to '{output_filename}': {e}")


if __name__ == "__main__":
    main()
