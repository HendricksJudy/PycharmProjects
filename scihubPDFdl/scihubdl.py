import urllib.request
import xlrd


def open_excel(file='sigcomm.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))
# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行  ，by_index：表的索引
def excel_table_byindex(file='sigcomm.xls', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows


    filenames = []
    urls = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            filenames.append(row[0])
            urls.append(row[1])


    list = [filenames, urls]  # url
    return list





if __name__ == "__main__":
    tables = excel_table_byindex()  # 根据索引获取Excel表格中的数据
    nrows = len(tables[1])
    add=''
    add1='C:\sd\PaperDownload\sigcomm\SDN\\'
    add2='C:\sd\PaperDownload\sigcomm\Security\\'
    add3= 'C:\sd\PaperDownload\sigcomm\VANET\\'
   for i in range(nrows):
        file_name = add+tables[0][i]+'.pdf'
        url = tables[1][i]
       u = urllib.request.urlopen(url)
        f = open(file_name, 'wb')
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            f.write(buffer)
        f.close()
        print("Sucessful to download " + " " + file_name)


