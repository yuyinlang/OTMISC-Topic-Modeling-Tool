import multiprocessing
import pprint
import re
import time
import types
import unicodedata
import unittest
from functools import reduce, partial
from typing import List, Tuple

import contractions
from nltk import RegexpTokenizer, WordNetLemmatizer
from nltk.corpus import stopwords

english_stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')


def list_available_prep_functions(exclude: Tuple[str] = ('run', 'list_available_prep_functions')):
    available_functions = [var for var in globals() if isinstance(globals()[var], types.FunctionType)]
    available_functions = [func for func in available_functions if func not in exclude]  # Exclude Passed Funcs
    available_functions = [func for func in available_functions if not func.startswith('__')]  # Exclude Private Funcs
    return available_functions


def __split_iterable_on_condition(condition_callable, iterable):
    trues = []
    falses = []
    for item in iterable:
        if condition_callable(item):
            trues.append(item)
        else:
            falses.append(item)
    return trues, falses


def __is_tokenized_method(func_name):
    return func_name.startswith('lemmatize') or 'stop_words' in func_name


def __tokenize(s): return tokenizer.tokenize(s)


def __glue(words): return ' '.join(words).strip()


def to_lowercase(text): return text.lower()


def standardize_accented_chars(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')


def remove_url(text):
    text = re.sub(r'https?\S+', '', text)
    return re.sub(r'www\S+', '', text)


def expand_contractions(text): return ' '.join([contractions.fix(word) for word in text.split()])


def remove_mentions(text): return re.sub(r'@\S*', '', text)


def remove_hashtags(text): return re.sub(r'#\S*', '', text)


def keep_only_alphabet(text): return re.sub(r'[^a-zA-Z]', ' ', text)


def remove_new_lines(text): return re.sub(r"\\n", " ", text)


def remove_extra_spaces(text): return ' '.join(text.split())


def remove_html_tags(text): return re.sub(r'<.*?>', ' ', text)


def remove_english_stop_words(tokenized_text: List[str]):
    return list(filter(lambda word: word not in english_stop_words, tokenized_text))


def lemmatize(tokenized_text: List[str], pos='n'):
    return [lemmatizer.lemmatize(word, pos) for word in tokenized_text]


def lemmatize_verb(tokenized_text: List[str]):
    return lemmatize(tokenized_text, pos='v')


def lemmatize_noun(tokenized_text: List[str]):
    return lemmatize(tokenized_text, pos='n')


def lemmatize_adjective(tokenized_text: List[str]):
    return lemmatize(tokenized_text, pos='a')


class TestUtils(unittest.TestCase):
    def test_all(self):
        # to_lowercase
        capital_str = 'IN CHINESE WE CALL CAPITALIZATION AS BIG WRITTING, IN GERMAN AS WELL.'
        lower_str = 'in chinese we call capitalization as big writting, in german as well.'
        self.assertTrue(lower_str == to_lowercase(capital_str))

        # standardize_accented_chars
        str_before = 'sómě words such as résumé, café, prótest, divorcé, coördinate, exposé, latté.'
        str_after = 'some words such as resume, cafe, protest, divorce, coordinate, expose, latte.'
        self.assertTrue(str_after == standardize_accented_chars(str_before))

        # remove_url
        str_before = 'using https://www.google.com/ as an example'
        str_after = 'using  as an example'
        self.assertTrue(str_after == remove_url(str_before))

        # expand_contractions
        str_before = "Don't is the same as do not"
        str_after = 'Do not is the same as do not'
        self.assertTrue(str_after == expand_contractions(str_before))

        # remove_mentions
        str_before = 'Some random @abc and #def'
        str_after = 'Some random  and #def'
        self.assertTrue(str_after == remove_mentions(str_before))

        # remove_tags
        str_before = 'Some random @abc and #def'
        str_after = 'Some random @abc and '
        self.assertTrue(str_after == remove_hashtags(str_before))

        # keep_only_alphabet
        str_before = 'Just a bit more $$processing required.Just a bit!!!'
        str_after = 'Just a bit more   processing required Just a bit   '
        self.assertTrue(str_after == keep_only_alphabet(str_before))

        # remove_english_stop_words
        str_before = 'Test this text to see which are stop words.'
        str_after = 'Test text see stop words .'
        self.assertTrue(str_after == remove_english_stop_words(str_before))

        # lemmatize
        str_before = 'apples, bananas and pears are common fruits that are eaten by humans.'
        str_after = 'apple , banana and pear are common fruit that are eaten by human .'
        self.assertTrue(str_after == lemmatize(str_before))

        # remove_extra_spaces
        str_before = ' Too                    much spaces   in  between!           '
        str_after = 'Too much spaces in between!'
        self.assertTrue(str_after == remove_extra_spaces(str_before))

        # remove_new_lines
        str_before = '“One,\\n\n\nTwo-hoo,\n\nThrrrrreee.”\\n\n\nThree.'
        str_after = '“One,Two-hoo,Thrrrrreee.”Three.'
        self.assertTrue(str_after == remove_new_lines(str_before))


def __instance_preprocess(a_str: str, str_methods: Tuple[str], tokenized_methods: Tuple[str] = None) -> str:
    a_str = reduce(lambda res, func: globals()[func](res), str_methods, a_str)
    if tokenized_methods:
        a_str = reduce(lambda res, func: globals()[func](res), tokenized_methods, a_str)
    return a_str


def __preprocess(data: List[str], str_methods: Tuple[str], tokenized_methods: Tuple[str] = None) -> List[str]:
    print(f'[INFO] These string preprocessing methods will be applied to the data in order:')
    pprint.pprint(str_methods, indent=3, width=40)
    if tokenized_methods:
        print(f'[INFO] Then, these tokenized preprocessing methods will be applied to the data in order:')
        pprint.pprint(tokenized_methods, indent=3, width=40)
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    return pool.map(partial(__instance_preprocess, str_methods=str_methods, tokenized_methods=tokenized_methods), data)


def __check_functions_validity(prep_functions: List[str]):
    all_funcs = set(list_available_prep_functions())

    if not set(prep_functions).issubset(all_funcs):
        print(f'[ERROR] Given functions:{prep_functions}, available functions:{all_funcs}.')
        raise ValueError(f'These functions are not available:{set(prep_functions).difference(all_funcs)}.')


def run(data: List[str], prep_functions: List[str]) -> List[str]:
    if not prep_functions:
        print(f'[WARN] Preprocessing functions are empty or None, given:"{prep_functions}", preprocessing is skipped.')
        return data
    __check_functions_validity(prep_functions=prep_functions)

    print(f'[INFO] Available Preprocessing Functions in the Module:{list_available_prep_functions()}')

    tokenized_funcs, str_funcs = __split_iterable_on_condition(__is_tokenized_method, iterable=prep_functions)
    if tokenized_funcs:
        tokenized_funcs = ['__tokenize'] + tokenized_funcs + ['__glue']
    tokenized_funcs, str_funcs = tuple(tokenized_funcs), tuple(str_funcs)

    t_0 = time.time()
    print(f'[INFO] Preprocessing starting..')
    preprocessed_data = __preprocess(data, str_methods=str_funcs, tokenized_methods=tokenized_funcs)
    print(f'[INFO] Preprocessing completed in {round(time.time() - t_0, 3)} seconds..')
    return preprocessed_data


def __test_tweets(data_name='crisis_12'):
    from utils import load_documents
    data, _ = load_documents(data_name)

    run(data=data, prep_functions=[
        'to_lowercase',
        'standardize_accented_chars',
        'remove_url',
        'expand_contractions',
        'remove_mentions',
        'remove_hashtags',
        'keep_only_alphabet',
        'remove_english_stop_words',
        'lemmatize_noun'
    ])


def __test_yahoo_answers(data_name='yahoo'):
    from utils import load_documents
    data, _ = load_documents(data_name)
    run(data=data, prep_functions=[
        'remove_html_tags',
        'remove_url',
        'remove_new_lines',
        'to_lowercase',
        'remove_english_stop_words',
        'lemmatize_verb',
        'lemmatize_noun',
        'lemmatize_adjective'
    ])


if __name__ == '__main__':
    __test_tweets(data_name='crisis_12')
    __test_yahoo_answers(data_name='yahoo')
