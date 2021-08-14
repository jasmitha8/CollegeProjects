import gspread
gc=gspread.service_account(filename='keys.json')
sh=gc.open_by_key('1t1HsHG99bcLS4oH1bNLMNKYx6WC9Gu9fh_vJgDqtg0Y')
worksheet=sh.sheet1
res=worksheet.get_all_values()

links=[]
for i in res[1:]:
    links.append(i[1])