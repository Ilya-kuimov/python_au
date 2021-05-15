import matplotlib.pyplot as plt
from datetime import datetime


def open_file(file='dataset.txt'):
    ouf = open(file)
    data = ouf.readlines()
    ouf.close()
    return data


def sort_by_date(data):
    headers = data.pop(0).strip(' ').strip('\n').split(',')
    info = []
    for elem in data:
        info.append(dict(zip(headers, elem.strip().split(','))))
    for elem in info:
        elem['resource'] = int(elem['resource'])
        elem['count'] = int(elem['count'])
        elem['date'] = datetime.strptime(elem['date'], '%Y-%m').date()
    sorted_info = sorted(info, key=lambda x: x['date'])
    return sorted_info


def sort_by_resource(sorted_info):
    resources = []
    for elem in sorted_info:
        resources.append(elem['resource'])
    resources.sort()
    unique_resources = list(set(resources))
    res_by_list = []
    for i in unique_resources:
        res_by_list.append(list(filter(lambda elem: elem['resource'] == i, sorted_info)))
    return res_by_list


def create_plot(res_by_list):
    abscissa = []
    ordinate = []
    staff = input()
    num_of_resource  = int(input())
    if staff != 'None':
        for elem in res_by_list:
            for dc in elem:
                    if dc['staff_id'] == staff and dc['resource'] == num_of_resource:
                        abscissa.append(dc['date'])
                        ordinate.append(dc['count'])
    else:
        for elem in res_by_list:
            for dc in elem:
                    if dc['resource'] == num_of_resource:
                        abscissa.append(dc['date'])
                        ordinate.append(dc['count'])
    if staff != 'None':
        plt.title(staff)
    else:
        plt.title(num_of_resource)
    plt.xlabel('date')
    plt.ylabel('count')
    plt.plot(abscissa, ordinate)
    plt.show()


def main(file):
    data_str = open_file(file)
    sorted_info = sort_by_date(data_str)
    res_by_list = sort_by_resource(sorted_info)
    create_plot(res_by_list)

#if you want info without staff, type 'None', 'number of resource'
#if you want info with staff, type 'Name of staff', 'number of resource'

if __name__ == '__main__':
    main('dataset.txt')