#Long Live Spock
from jira import JIRA
options={
    'server':'https://jira.successfactors.com/',
    }
while True:
    try:
        usrname=raw_input("enter ur username:")
        passwd=raw_input("enter ur password:")
        jira=JIRA(options,basic_auth=(usrname,passwd),validate=True)
        break
    except Exception:
        print 'wrong username or password.Please try again'
        continue
lists=[]
patch_prod=raw_input("enter new patch number for production and dev environments(eg:403):")
patch_sales=raw_input("enter new patch number for sales environment(eg:403):")
DC_num=[2,4,8,10,12,15,17,18,19]
print 'enter implementation date in yyyy,mm,dd order and enter friday\'s date,script will adjust the date and time by itself'
yr=raw_input('year:')
mnth=raw_input('month:')
day=raw_input('day:')
dayt=str(int(day)-1)
days=str(int(day)+1)
day_splitt=[yr,mnth,dayt]
day_splitf = [yr,mnth,day]
day_splits=[yr,mnth,days]
datef='-'.join(day_splitf)
datet='-'.join(day_splitt)
dates='-'.join(day_splits)

#After creating CMSDs mail will be automatically sent to the recipients but this will work only in sap-internet and not sap-corporate because of firewall issue
def send_mail(recipient, subject, message): 

    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    username = "vishwanathsandesh@gmail.com"
    password = "vanithavishwanath"
    print 'preparing for mailing all the CMSDs created'
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = ",".join(recipient)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    try:
        print 'sending mail to ' + ",".join(recipient) + ' on ' + subject

        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, recipient, msg.as_string())
        mailServer.close()

    except Exception:
        print 'error! mail not set' 
        
def assign_values(a,b,c,d,data_protection,start,end,patch_no):
    smry="JAM "+a +" "+ d + " | Weekly Patch" +" | Update Jam to R"+str(patch_no)
    descript="JAM "+a +" "+ d + " | Update Jam to R"+str(patch_no)
    test_details="QA Team will do validation using Watir tool to confirm that the functionality of the Application works fine."
    justification="update jam to R"+str(patch_no)
    imp_steps="""Note: [ There are special deployment instructions which is announced to Ops and finalized every Thursday after Go/No-GO meeting by Engineering Team] 

                    Steps to be performed during the Deployment: 

                    1. Disable pingdom for Respective DC's checks at the implementation starting time 

                    2. Deploy the code on JAM DC Production Server through Devops node. 

                    [Note: Here XX should be replaced by respective release number and appropiate Datacenter] 

                    -=-=-=-=-=-= starting RXXX Deployment on DCXX -=-=-=-=-=-= 

                    Login to Devops node of the respective DC and execute the below commands: 

                    cd ~/code/jam<>/ct && cap -S instance=jam<> production deploy:web:disable; 

                    -------complete------ 


                    Step### 1. Prepare the CT environment for deployment 
                    cd ~/code/jam<>/ct && cap -S instance=jam<> production deploy:push_release 

                    -------complete------ 


                    Step### 2. Prepare the PS environment for deployment 
                    cd ~/code/jam<>/ps && cap -S instance=jam<> production deploy:push_release 


                    --------- complete-------- 


                    Step### 3. Prepare the OpenSocial environment for deployment 
                    cd ~/code/jam<>/opensocial && bundle exec cap -S instance=jam<> production deploy:push_release; 


                    Step### 4. Flush memcache 
                    cd ~/code/jam<>/ct && cap -S instance=jam<> production deploy:flush_memcache ; 

                    --------complete---------- 


                    ######## verify deployed code for both ct and ps ######## 

                    cd ~/code/jam<>/ct && cap -S instance=jam<> production deploy:verify_release 

                    cd ~/code/jam<>/ps && cap -S instance=jam<> production deploy:verify_release 

                    #########Restart Rpush######### 
                    cd ~/code/jam<>/ct && cap -S instance=<> production rpush:restart 
                    ################################ 

                    cd ~/code/jam<>/ct && cap -q -S instance=jam=<> production diagnostics:all; 

                    ################################################ 



                    -=-= Wait for a 2 mins before executing web:enable -=-=- 


                    Step### 5. Enable the site if it was disabled 
                    cd ~/code/jam<>/ct && cap -S instance=<> production deploy:web:enable 

                    --------complete-------- 


                    echo " RXXX now live in dcXX `date` " 

                    -=-=-=--= RXXX is now live in dcXX -=-=-=--= 
                    -=-=-=--= Testing can start -=-=-=--= 


                    ###CT - After testing starts 


                    ## Exit script logging 
                    exit 

                    ## Kill permanently this tmux session 
                    tmux kill-session -t <name> 


                    ## To detach from a session and keep it running in the background and reattach in future 
                    ## tmux detach 



                    -=-= Enabled Pingdom for <DC> -=-= 


                    3. Once all the deployment commands finished successfully, check the URL availability. URL link is given below: 
                    https://jam2.sapjam.com/ 
                    https://developer.sapjam.com/ 
                    https://jamsalesdemo2.sapjam.com 

                    https://jam4.sapjam.com/ 
                    https://jam8.sapjam.com/ 
                    https://jam10.sapjam.com/ 
                    https://jam12.sapjam.com/ 
                    https://demo.sapjam.com 
                    https://jamsalesdemo8.sapjam.com 

                    4. Enable pingdom for Respective DC's checks."""
    back_steps="""Roll back to previous build, will take around 30 minutes which is within the maintenance window. 

                    In the case of Jam, if there is a problem with the deployment, it will also often cause a problem with the rollback, i.e. networking problems, infra problems with a particular VM etc. So the "rollback" in the traditional sense will not work and needs to be handled in a custom way. 

                    If there is a desire to rollback for code reasons, our approach is different from most applications because we deploy every week. Thus the amount of change is very small and a traditional rollback is very unexpected. So our approach is: 

                    Strategy 1- identify and fix the problem, with a patch if needed (patches are not always needed, for example, betas can be turned off). 

                    Strategy 2- if possible, run the old code with the new schema i.e. code rollback only. We should make sure this is possible always. @Harsimran Maan has tests in prep ensuring that this is so. 

                    Strategy 3- rollback db migration and code. This is such a rare event. 

                    In any case, our approach to absolutely minimal deployments means that if there is any problem to the deployment then Jam Engineering needs to be involved and present."""
    validate="QA Team will do validation using Watir tool to confirm that the functionality of the Application works fine"
                    
    values = {
        'project' : 'CMSD', 
        'issuetype' : 'Change Request', 
        'customfield_16584' : { 'value' : 'Low' }, 
        'summary' : smry, 
        'customfield_17680' : { 'value' : 'Low' },
        'customfield_17681' : { 'value' : 'Low' },
        'customfield_17682' : { 'value' : 'Low' }, 
        'customfield_17683' : { 'value' : 'Low' }, 
        'customfield_17684' : { 'value' : 'Low' }, 
        'customfield_16583' : {'value':'App', 'child': {'value':'Update/Upgrade'}},  
        'components' : [{'name': 'JAM'}], 
        'customfield_15282' : {'value':data_protection},
        'customfield_10802' : { 'value' : a }, 
        'customfield_16590' : { 'id' : Ztime },
        'customfield_10842' : { 'id' : c }, 
        'customfield_16794' : {'value':'None'},
        'customfield_17055' : {'value':'No'}, 
        'customfield_17056' : { 'value' : 'Not Required' }, 
        'customfield_17057' : { 'value' : 'No' }, 
        'customfield_16814' : start,  
        'customfield_16815' : end,
        #'customfield_17282' : "09/Dec/16 12:00 AM EST (All US/CA)",
        #'customfield_17283' : "09/Dec/16 01:00 AM EST (All US/CA)",
        'description' : descript, 
        'customfield_17426' : test_details, 
        'customfield_17427' : justification, 
        'customfield_17058' : imp_steps, 
        'customfield_16800' : back_steps,
        'customfield_16801' : validate, 
        'customfield_16802' : { 'name' : 'flui' },
        'customfield_17059' : [{ 'value' : 'TechOwn - JAM' }], 
        'customfield_17060' : [{ 'value' : 'BusOwn - JAM' }], 
                    }
    new_issue = jira.create_issue(fields=values)
    jira.assign_issue(new_issue, 'sureshkumara')
    #print new_issue.key
    key=a+" "+j+":"+str(new_issue.key)
    #print key
    lists.append(key)


for i in range(9):
    DC=DC_num[i]
    if DC==2:
        actual_DC="DC"+str(DC)+' - '+"Amsterdam2"
        Ztime="21745"
        data='European Union Data Protection'
        env=['Prod','Sales','Dev']
        for j in env:
            if j=='Prod':
                actual_env='11668'
                start=datet+'T09:30:00.000-0700'
                end=datet+'T10:30:00.000-0530'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_prod)
            elif j=='Sales':
                actual_env='11930'
                start=datef+'T06:30:00.000-0700'
                end=datef+'T07:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_sales)
            elif j=='Dev':
                actual_env='11668'
                start=datef+'T11:30:00.000-0700'
                end=datef+'T12:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_prod)
    elif DC==4:
        actual_DC="DC"+str(DC)+' - '+"Chandler1"
        Ztime="21744"
        data='No Data Protection Regulation'
        env=['Prod','Sales']
        for j in env:
            if j=='Prod':
                actual_env='11668'
                start=datet+'T11:30:00.000-0700'
                end=datet+'T12:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_prod)
            elif j=='Sales':
                actual_env='11930'
                start=datef+'T07:30:00.000-0700'
                end=datef+'T08:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_sales)
            elif j=='Dev':
                actual_env='11668'
                assign_values(actual_DC,Ztime,actual_env,j,data)
    elif DC==8:
        actual_DC="DC"+str(DC)+' - '+"Ashburn1"
        Ztime="21744"
        data='No Data Protection Regulation'
        env=['Prod','Sales']
        for j in env:
            if j=='Prod':
                actual_env='11668'
                start=datet+'T11:30:00.000-0700'
                end=datet+'T12:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_prod)
            elif j=='Sales':
                actual_env='11930'
                start=datef+'T07:30:00.000-0700'
                end=datef+'T08:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_sales)
            elif j=='Dev':
                actual_env='11668'
                assign_values(actual_DC,Ztime,actual_env,j,data)
    elif DC==10:
        actual_DC="DC"+str(DC)+' - '+"Sydney1"
        Ztime="21746"
        data='No Data Protection Regulation'
        env=['Prod']
        for j in env:
           if j=='Prod':
                actual_env='11668'
                start=datef+'T17:30:00.000-0700'
                end=datef+'T18:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_prod)
           elif j=='Sales':
                actual_env='11930'
                assign_values(actual_DC,Ztime,actual_env,j,data)
           elif j=='Dev':
                actual_env='11668'
                assign_values(actual_DC,Ztime,actual_env,j,data)
    elif DC==12:
        actual_DC="DC"+str(DC)+' - '+"Rot1"
        Ztime="21745"
        data='European Union Data Protection'
        env=['Prod']
        for j in env:
            if j=='Prod':
                actual_env='11668'
                start=datet+'T09:30:00.000-0700'
                end=datet+'T10:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_prod)
            elif j=='Sales':
                actual_env='11930'
                assign_values(actual_DC,Ztime,actual_env,j,data)
            elif j=='Dev':
                actual_env='11668'
                assign_values(actual_DC,Ztime,actual_env,j,data)
    elif DC==15:
        actual_DC="DC"+str(DC)+' - '+"Shanghai1"
        Ztime="21747"
        data='No Data Protection Regulation'
        env=['Prod']
        for j in env:
            if j=='Prod':
                actual_env='11668'
                start=datef+'T13:30:00.000-0700'
                end=datef+'T14:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_prod)
            elif j=='Sales':
                actual_env='11930'
                assign_values(actual_DC,Ztime,actual_env,j,data)
            elif j=='Dev':
                actual_env='11668'
                assign_values(actual_DC,Ztime,actual_env,j,data)
    elif DC==17:
        actual_DC="DC"+str(DC)+' - '+"Toronto1"
        Ztime="21744"
        data='No Data Protection Regulation'
        env=['Prod']
        for j in env:
           if j=='Prod':
                actual_env='11668'
                start=datet+'T11:30:00.000-0700'
                end=datet+'T12:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
           elif j=='Sales':
                actual_env='11930'
                assign_values(actual_DC,Ztime,actual_env,j,data)
           elif j=='Dev':
                actual_env='11668'
                assign_values(actual_DC,Ztime,actual_env,j,data)
    elif DC==18:
        actual_DC="DC"+str(DC)+' - '+"Moscow1"
        Ztime="21748"
        data='No Data Protection Regulation'
        env=['Prod']
        for j in env:
            if j=='Prod':
                actual_env='11668'
                start=datet+'T12:30:00.000-0700'
                end=datet+'T13:30:30.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end)
            elif j=='Sales':
                actual_env='11930'
                assign_values(actual_DC,Ztime,actual_env,j,data)
            elif j=='Dev':
                actual_env='11668'
                assign_values(actual_DC,Ztime,actual_env,j,data)
    
    elif DC==19:
        actual_DC="DC"+str(DC)+' - '+"Sao Paulo1"
        Ztime="21749"
        data='No Data Protection Regulation'
        env=['Prod']
        for j in env:
            if j=='Prod':
                actual_env='11668'
                start=datet+'T13:30:00.000-0700'
                end=datet+'T14:30:00.000-0700'
                assign_values(actual_DC,Ztime,actual_env,j,data,start,end,patch_prod)
            elif j=='Sales':
                actual_env='11930'
                assign_values(actual_DC,Ztime,actual_env,j,data)
            elif j=='Dev':
                actual_env='11668'
                assign_values(actual_DC,Ztime,actual_env,j,data)
       

print lists
print 'converting lists of CMSDs into string'
string=','.join(lists)
send_mail(['monalisa.karmakar@sap.com','aniket.shekhar.sharma@sap.com','sandesh.vishwanath@sap.com','s.appuswaami@sap.com'], 'CMSD tickets for next JAM release', string)
