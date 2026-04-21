class CustomCount:
    @staticmethod
    def count(text, sub):
        if not sub:
            return len(text) + 1

        count = 0
        start = 0
        sub_len = len(sub)

        while start <= len(text) - sub_len:
            match = True
            for i in range(sub_len):
                if text[start + i] != sub[i]:
                    match = False
                    break

            if match:
                count += 1
                start += sub_len
            else:
                start += 1
        return count



print(CustomCount.count("hello hello hello", "hello"))
print(CustomCount.count("aaaaa", "aa"))
