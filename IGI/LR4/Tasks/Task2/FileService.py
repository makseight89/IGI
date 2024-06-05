from zipfile import ZipFile, ZIP_DEFLATED


class FileService:
    @staticmethod
    def read_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except IOError:
            print("���������� ������� ����")
            return None

    @staticmethod
    def save_to_file(file_path, data):
        try:
            with open(file_path, 'w') as file:
                file.writelines(data)
        except IOError:
            print("���������� �������� � ����")

    @staticmethod
    def archive_file(file_path, zip_path):
        try:
            with ZipFile(zip_path, 'w', compression=ZIP_DEFLATED, compresslevel=2) as archive:
                archive.write(file_path)
        except IOError:
            print("���������� ������� ����")

    @staticmethod
    def get_archive_info(zip_path):
        try:
            with ZipFile(zip_path) as archive:
                print('���������� � ������:')
                for info in archive.infolist():
                    file_type = 'Folder' if info.is_dir() else 'File'
                    print(f'��� {file_type}')
                    print(f'������: {info.file_size}, ���: {info.filename}, ����: {info.date_time}')
        except IOError:
            print("���������� ��������� ����������")