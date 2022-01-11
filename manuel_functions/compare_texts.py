import diff_match_patch as dmp_module


def compare_texts(text1: str, text2: str) -> list:
    dmp = dmp_module.diff_match_patch()
    diff = dmp.diff_main(text1, text2)
    dmp.diff_cleanupSemantic(diff)
    return diff


if __name__ == "__main__":
    print(compare_texts("Hello World", "Goodbye World."))
