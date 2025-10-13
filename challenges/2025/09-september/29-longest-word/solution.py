from module_test import do_test

def get_longest_word(sentence: str) -> str:
    words = sentence.replace(".", "").split(" ")
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

do_test(function_name="get_longest_word", should_return="coding", sentence="coding is fun")
do_test(function_name="get_longest_word", should_return="educational", sentence="Coding challenges are fun and educational.")
do_test(function_name="get_longest_word", should_return="sentence", sentence="This sentence has multiple long words.")
