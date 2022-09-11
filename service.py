import datetime
from datetime import time
import time
from requests_html import HTMLSession

session = HTMLSession()


class page_data:
    title: str
    description: str
    h1 = []
    h2 = []
    h3 = []
    h4 = []
    h5 = []
    h6 = []


class Service:
    while_true = True
    list_head = []
    head = []
    iid = 0
    value = []

    def start(self, table, host: str):
        self.list_head.append(host)
        if host not in self.head:
            self.head.append(host)
            start_time = time.time()
            r = session.get(host)
            start_time = time.time() - start_time
            code = r.status_code
            for i in sorted(r.html.absolute_links):
                if self.while_true is False:
                    self.list_head = []
                    self.head = []
                    return 1
                if str(i).find(host) != -1 and str(i).find('tel') == -1 and str(i).find('mail') == -1 and str(
                        i) != host and str(i) != host + '/':
                    if code == 200:
                        table.insert(parent='', index='end', iid=self.iid, values=(i, code, start_time),
                                     tags=('green',))
                    elif code == 400:
                        table.insert(parent='', index='end', iid=self.iid, values=(i, code, start_time), tags=('red',))
                    self.value.append(self.get_values_page(r))
                    self.iid += 1
                    if i not in self.list_head:
                        self.start(table, i)

    def get_values_page(self, page):
        val = page_data()
        # get title
        temp = page.html.find('title', first=True)
        val.title = temp.full_text

        temp = page.html.find('meta[name="description"]', first=True)
        val.description = temp.attrs['content']

        for i in page.html.find('h1'):
            val.h1.append(i.full_text)

        for i in page.html.find('h2'):
            val.h2.append(i.full_text)

        for i in page.html.find('h3'):
            val.h3.append(i.full_text)

        for i in page.html.find('h4'):
            val.h4.append(i.full_text)
        return val

    def get_values_by_id(self, iid):
        return self.value[iid]


service = Service()
