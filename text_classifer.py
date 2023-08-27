import os
import re
import random
import spacy
from spacy.training.example import Example
from tqdm import tqdm
from sklearn.metrics import f1_score


class TextClassifer:
    def __init__(self, label_list=['tg', 'vk', 'yt', 'zn'], show_info=False):

        # Инициализвация модели

        # config = Config().from_disk('../config/base_config.cfg') # "en_core_web_lg"
        # self.nlp = spacy.blank('en', config=config)
        try:
            self.nlp = spacy.load(os.path.join('models', 'model_text_cat'))
            spacy.prefer_gpu()
        except:
            print('Модель не определена')
            spacy.prefer_gpu()
            self.nlp = spacy.blank('xx')
            self.nlp.add_pipe('tok2vec')
            self.nlp.add_pipe('textcat')

        self.textcat = self.nlp.get_pipe('textcat')

        for label in label_list:
            self.textcat.add_label(label)

        if show_info:
            print(f'Pipline: {self.nlp.pipe_names}')
            print(self.nlp.analyze_pipes(pretty=True))

    def clear_string(self, s):  # Функция для очистки
        s = ' '.join(re.sub(r'[^а-яА-ЯёЁa-zA-Z\d:-]', ' ', str(s).lower()).split())
        return s

    def create_string(self, val):  # Функция для создания строки
        val = [str(x) for x in val if (x != None)]  # Берём все кроме пустых строк
        val = '; '.join(str(x) for x in val)  # Создаём строку элемента
        return val

    def fit(self, epoch=10, data_train=None, batch_size=4, val=None):
        optimizer = self.nlp.begin_training()

        other_pipes = [pipe for pipe in self.nlp.pipe_names if pipe != 'textcat']
        with self.nlp.disable_pipes([]):  # *other_pipes
            for epoch in tqdm(range(1, epoch + 1)):
                random.shuffle(data_train)
                losses = {}
                for batch in spacy.util.minibatch(data_train, size=batch_size):
                    example = None
                    for text, annotations in batch:
                        doc = self.nlp.make_doc(text)
                        example = Example.from_dict(doc, annotations)
                        self.nlp.update([example], sgd=optimizer, losses=losses, drop=0.2)
                if val:
                    metric = self.evaluate(val)
                    print(metric)
                    print('Losses', losses)
                else:
                    print('Losses', losses)

        self.nlp.to_disk(os.path.join('models', 'model_text_cat'))

    def predict(self, data):
        '''
        Функция определения нужного списка.

        :param data: Двумерный список Текстов.
        :type data: .

        :return: Список [tg', 'vk', 'yt', 'zn'] для каждого элемента.
        :rtype: list.
        '''
        pred = []
        for d in data:
            # d_clear = self.create_string(d)
            # d_clear = self.clear_string(d_clear)
            doc = self.nlp(d)
            pred.append(max(doc.cats, key=doc.cats.get))

            # if max(doc.cats, key=doc.cats.get) == "POSITIVE":
            # pred.append([str(x).lower() for x in d])
            # pred.append(max(doc.cats, key=doc.cats.get))

        return pred

    def evaluate(self, data):
        '''
        Функция подсчёта метрики.

        :param data: Список кортежей в формате text_cat spacy.
        :type data: [('порт выхода rizhao qingdao shanghaien океанского порта эксп оформление в основном pol xiamen dalian lianyungang shantou l',
  {'cats': {'POSITIVE': 1}})].

        :return: Accuracy.
        :rtype: dict.
        '''
        count = len(data)
        count_true = 0

        true_data = []
        predict = []

        # ('порт прибытия спб пкт спб пкт спб пкт', {'cats': {'POSITIVE': 1}}),

        categoric = {'tg': 0, 'vk': 1, 'yt': 2, 'zn': 3}

        for elem in data:  # Пробегаемся по каждому элементу
            doc = self.nlp(elem[0])  # Обрабатываем текст
            pred = max(doc.cats, key=doc.cats.get)
            true = list(elem[1].get('cats').keys())[0]

            if pred == true:
                count_true += 1

            true_data.append(categoric.get(true))
            predict.append(categoric.get(pred))

        return {'Accuracy: ': count_true / count, 'F1-weighted': f1_score(true_data, predict, average='weighted')}