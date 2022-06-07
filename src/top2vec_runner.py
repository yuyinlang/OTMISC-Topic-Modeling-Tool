import time
from collections import OrderedDict
from typing import List, Dict, Any, Tuple

from top2vec import Top2Vec

from utils import load_documents


def print_params(dataset_dir: str, speed: str, embedding_model: str, num_topics: int, data_col: str):
    print('[INFO] Top2Vec Parameters:')
    print(f'    > Input Dataset Directory:"{dataset_dir}".')
    print(f'    > Input Dataset Data Column:"{data_col}".')
    print(f'    > Model Speed:"{speed}".')
    print(f'    > Model Embedding Model:{embedding_model}.')
    print(f'    > Pre-specified Number of Topics:{num_topics}.')


def print_topic_stats(stats: List[Dict[str, Any]]) -> None:
    for stat in stats:
        print(f'[INFO] Topic #{str(stat["topic_num"]).zfill(2)}:')
        print(f'     > From Reduced Model:{stat["reduced"]}.')
        print(f'     > Topic Size:{stat["topic_size"]}.')
        print(f'     > Topic Words:', str(stat['topic_words']).replace('\n', '\n\t\t'))
        print(f'     > Topic Word Scores:', str(stat['word_scores']).replace('\n', '\n\t\t'))


def get_topic_stats(model_t2v: Top2Vec, is_reduced: bool = False) -> List[Dict[str, Any]]:
    num_topics = model_t2v.get_num_topics(reduced=is_reduced)
    topic_sizes, topic_nums = model_t2v.get_topic_sizes(reduced=is_reduced)
    topic_words, word_scores, _ = model_t2v.get_topics(num_topics=num_topics, reduced=is_reduced)

    stats = []
    for tn, ts, tw, ws in zip(topic_nums, topic_sizes, topic_words, word_scores):
        stats.append(OrderedDict([
            ('reduced', is_reduced),
            ('topic_num', tn),
            ('topic_size', ts),
            ('topic_words', tw),
            ('word_scores', ws)
        ]))
    return stats


def run(dataset_dir: str, speed: str, embedding_model: str, num_topics: int = None, data_col: str = None) -> Tuple:
    print_params(dataset_dir, speed, embedding_model, num_topics, data_col)
    print(f'[INFO] Top2Vec is running for dataset directory:"{dataset_dir}".')

    documents = load_documents(dataset_dir, data_col)
    time_process_start = time.time()
    model = Top2Vec(documents, speed=speed, workers=8, embedding_model=embedding_model)
    non_reduced_num_topics = model.get_num_topics(reduced=False)
    print(f'[INFO] Original (Non-reduced) Number of Topics: {non_reduced_num_topics}.')
    topic_stats = get_topic_stats(model_t2v=model, is_reduced=False)
    if num_topics is not None:
        if non_reduced_num_topics > num_topics:
            model.hierarchical_topic_reduction(num_topics=num_topics)
            topic_stats = get_topic_stats(model_t2v=model, is_reduced=True)
        else:
            print('[WARN] # of topics is pre-specified but non_reduced_num_topics <= num_topics, so not reduced!')
            print(f'   > non_reduced_num_topics:{non_reduced_num_topics}, given num_topics:{num_topics}!')
            time.sleep(3)
    duration_secs = float('%.3f' % (time.time() - time_process_start))
    print_topic_stats(stats=topic_stats)

    print(f'[INFO] Top2Vec successfully terminated for data:"{dataset_dir}".')
    return model, topic_stats


if __name__ == '__main__':
    # TODO: set "workers" parameter to the number of cores.
    # Alternatives: ['doc2vec', 'universal-sentence-encoder', 'universal-sentence-encoder-large',
    # 'universal-sentence-encoder-multilingual', 'universal-sentence-encoder-multilingual-large',
    # 'distiluse-base-multilingual-cased', 'all-MiniLM-L6-v2', 'paraphrase-multilingual-MiniLM-L12-v2']
    args = {
        'dataset_dir': './data/crisis_resource_01_labeled_by_paid_workers',
        'data_col': 'tweet_text',
        # 'dataset_dir': './data/crisis_resource_12_labeled_by_paid_workers',
        # 'data_col': 'text',
        # 'dataset_dir': './data/20news_bydate',
        'speed': 'fast-learn',  # Options: ['fast-learn', 'learn', 'deep-learn']
        'embedding_model': 'doc2vec',
        'num_topics': 4  # Options: None or integer
    }
    run(**args)
