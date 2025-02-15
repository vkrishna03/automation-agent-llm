
class LocalTools:

    def read_text_file(file_path: str) -> str:
        """
        Read content from a text file and return it as a string.
        
        Args:
            file_path (str): Path to the text file to read
            
        Returns:
            str: Content of the file
            
        Raises:
            FileNotFoundError: If file doesn't exist
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading file: {str(e)}")

