from zipfile import ZipFile, ZIP_DEFLATED


class FileService:
    @staticmethod
    def read_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except IOError:
            print("Невозможно считать файл")
            return None

    @staticmethod
    def save_to_file(file_path, data):
        try:
            with open(file_path, 'w') as file:
                file.writelines(data)
        except IOError:
            print("Невозможно записать в файл")

    @staticmethod
    def archive_file(file_path, zip_path):
        try:
            with ZipFile(zip_path, 'w', compression=ZIP_DEFLATED, compresslevel=2) as archive:
                archive.write(file_path)
        except IOError:
            print("Невозможно открыть файл")

    @staticmethod
    def get_archive_info(zip_path):
        try:
            with ZipFile(zip_path) as archive:
                print('Информация о файлах:')
                for info in archive.infolist():
                    file_type = 'Folder' if info.is_dir() else 'File'
                    print(f'Это {file_type}')
                    print(f'Размер: {info.file_size}, Имя: {info.filename}, Дата: {info.date_time}')
        except IOError:
            print("Невозможно прочитать информацию")