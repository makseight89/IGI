import re
from Tasks.Task2.FileService import FileService
from Tasks.Task import Task


class Task2(Task):
    @staticmethod
    def __analyze_sentence_types(text):
        pobud = len(re.findall(r"\!(\s|$)", text))
        povest = len(re.findall(r"\.(\s|$)", text))
        vopr = len(re.findall(r"\?(\s|$)", text))
        return pobud, povest, vopr

    @staticmethod
    def __average_sentence_length(text):
        sentences = re.findall(r"([^?!.]+)(\.|\!|\?)", text)
        total_length = 0
        for sentence in sentences:
            words = re.findall(r"\b[A-z]+\b", sentence[0])
            total_length += sum(len(word) for word in words)
        return total_length / len(sentences) if sentences else 0

    @staticmethod
    def __extract_words(text):
        return re.findall(r"\b[A-z]+\b", text)

    @staticmethod
    def __average_word_length(text):
        words = Task2.__extract_words(text)
        total_length = sum(len(word) for word in words)
        return round(total_length / len(words)) if words else 0

    @staticmethod
    def __words_of_length(text, length):
        return [word for word in Task2.__extract_words(text) if len(word) == length]

    @staticmethod
    def __every_7th_word(text):
        words = Task2.__extract_words(text)
        return [word for i, word in enumerate(words, start=1) if i % 7 == 0]

    @staticmethod
    def __count_smiles(text):
        return len(re.findall(r"(:|;)(\-*)(\(+|\)+|\[+|\]+)", text))

    @staticmethod
    def __extract_phone_numbers(text):
        return re.findall(r"\+37529\d{7}\b", text)

    @staticmethod
    def __words_with_specific_pattern(text):
        return re.findall(r"\b[A-z][bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ][aeiouyAEIOUY][A-z]*\b", text)

    @staticmethod
    def __count_consonant_ending_words(text):
        return len(re.findall(r"\b[A-z]*[bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ]\b", text))

    @staticmethod
    def __analyze_text(text):
        result = []
        pobud, povestv, vopr = Task2.__analyze_sentence_types(text)
        result.append(f"В тексте {pobud + povestv + vopr} предложений")
        result.append(f"Повествовательных: {povestv}")
        result.append(f"Побудительных: {pobud}")
        result.append(f"Вопросительных: {vopr}\n")

        av_sent_len = Task2.__average_sentence_length(text)
        result.append(f"Средняя длина предложения: {av_sent_len}")

        av_word_len = Task2.__average_word_length(text)
        result.append(f"Средняя длина слова: {av_word_len}")

        smiles_count = Task2.__count_smiles(text)
        result.append(f"Количество смайликов: {smiles_count}")

        phones = Task2.__extract_phone_numbers(text)
        result.append(f"Номера телефонов: {phones}")

        find_words = Task2.__words_with_specific_pattern(text)
        result.append(f"Слова, у которых вторая буква согласная, а третья – гласная: {find_words}")

        consonant_count = Task2.__count_consonant_ending_words(text)
        result.append(f"Число слов, заканчивающихся на согласную: {consonant_count}")

        av_len_words = Task2.__words_of_length(text, av_word_len)
        if av_len_words:
            result.append(f"Cлова, которые имеют среднюю длину: {av_len_words}")
        else:
            result.append(f"Слов длиной {av_word_len} символов в строке нет")

        ev_7th_words = Task2.__every_7th_word(text)
        result.append(f"Каждое 7-е слово: {ev_7th_words}")

        return "\n".join(result)

    @staticmethod
    def solve():
        source_path = 'Task2text.txt'
        dest_path = 'Task2answer.txt'
        archive_path = 'Task2archive.zip'

        text = FileService.read_from_file(source_path)
        if text:
            text = "".join(text)  # Конвертируем список строк в одну строку
            result = Task2.__analyze_text(text)
            FileService.save_to_file(dest_path, result)
            FileService.archive_file(dest_path, archive_path)
            FileService.get_archive_info(archive_path)