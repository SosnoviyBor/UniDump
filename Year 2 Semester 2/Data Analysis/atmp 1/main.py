def date_sorter():
    
    regex1 = '(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})'
    regex2 = '((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\S]*[+\s]\d{1,2}[,]{0,1}[+\s]\d{4})'
    regex3 = '(\d{1,2}[+\s](?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\S]*[+\s]\d{4})'
    regex4 = '((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\S]*[+\s]\d{4})'
    regex5 = '(\d{1,2}[/-][1|2]\d{3})'
    regex6 = '([1|2]\d{3})'
    full_regex = '(%s|%s|%s|%s|%s|%s)' %(regex1, regex2, regex3, regex4, regex5, regex6)
    parsed_date = df.str.extract(full_regex)
    parsed_date = parsed_date.iloc[:,0].str.replace('Janaury', 'January').str.replace('Decemeber', 'December')
    parsed_date = pd.Series(pd.to_datetime(parsed_date))
    parsed_date = parsed_date.sort_values(ascending=True).index
    return pd.Series(parsed_date.values)