def parse_date(date):
    '''
    Parses the date string provided by news Api to more readable form
    '''
    months={
    '01':'Jan',
    '02':'Feb',
    '03':'Mar',
    '04':'Apr',
    '05':'May',
    '06':'Jun',
    '07':'Jul',
    '08':'Aug',
    '09':'Sep',
    '10':'Oct',
    '11':'Nov',
    '12':'Dec'
    }
    dater,time=date.split('T')
    year,month,day=dater.split('-')
    hour,minute,sec=time.split(':')
    sec=sec[:-1]
    return day+'th'+' '+months[month]+' '+year+'  '+hour+':'+minute+':'+sec
    
def url_maker(domain,params):
    '''
    Generates url from domain and query parameters.
    
    domain :string: A string representing the url of the domain .Eg- https://www.google.com/?
    params :list of lists: [parameter_name,parameter_value]
    '''
    s=domain
    for i in range(len(params)):
        if i==0:
           s=s+str(params[i][0])+'='+str(params[i][1])
        else:
           s=s+'&'+str(params[i][0])+'='+str(params[i][1])
    return s