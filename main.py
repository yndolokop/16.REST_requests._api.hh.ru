import requests
import pprint
import json

url = 'https://api.hh.ru/vacancies'
p = 'Python'


def total_vacancy():
    params = {'text': f'{p}', 'page': 1, 'area': 1}
    result_total_vacancies = requests.get(url, params=params).json()
    total_vacancies = dict(keyword=p, count=result_total_vacancies['found'])
    return total_vacancies


def skills_search():
    final_list_of_counts = []
    skills_lst = ['Numpy', 'Pandas', 'Python', 'Django', 'Flask', 'Oracle', 'SQL', 'MS SQL', 'Git', 'Gitlab',
                  'Git GitLab', 'Confluence', 'CI/CD', 'html', 'css javascript', 'unittest OR pytest',
                  'Redis', 'asyncio', 'aiohttp', 'fastAPI', 'ORM', 'Memcached', 'Soap', 'Sentry']
    for i in skills_lst:
        params = {'text': f"NAME:({p}) AND DESCRIPTION:({i})", 'page': 1, 'area': 1}
        result_vacancies = requests.get(url, params=params).json()
        num_of_skill = result_vacancies['found']
        a = dict(name=i, count=num_of_skill, percent='{0:.1f}'.format(100*num_of_skill/total_vacancy()['count']))
        final_list_of_counts.append(a)
    return sorted(final_list_of_counts, key=lambda x: x['count'], reverse=True)


if __name__ == '__main__':
    b = dict(total_vacancy(), requirements=skills_search())
    pprint.pprint(b)
    with open('skills_list_count.json', 'w') as f:
        json.dump(b, f)



