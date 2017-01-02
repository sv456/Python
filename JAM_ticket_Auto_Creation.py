from jira import JIRA
options={
    'server':'https://jira.successfactors.com/',
    }
usrname=raw_input("enter ur username:")
passwd=raw_input("enter ur password:")
patch_no=raw_input("enter new patch number(eg:403):")
jira=JIRA(options,basic_auth=(usrname,passwd),validate=True)
date=raw_input('enter (enter only friday date and not satuday date program will adjust itself)implementation date in yyyy-mm-dd format:')
day_split = date.split('-')
next_day = int(day_split[2]) + 1
next_date = day_split[0] + "-" + day_split[1] + "-" + str(next_day)
print('only dates will be mentioned in the ticket please adjust the timing in each ticket')

DC = {
    "DC17" : {"Prod": "Friday"}, 
#    "DC4" : {"Sales" : "Saturday",  "Prod": "Friday"}, 
#    "DC2" : {"Sales": "Saturday" , "Prod": "Friday", "Developer": "Saturday"},
#    "DC8" : {"Sales": "Saturday",   "Prod": "Friday"},
#    "DC10" : {"Prod": "Friday"},
#    "DC12" : {"Prod": "Friday"},  
 #   "DC15" : {"Prod": "Friday"},
#    "DC18" : {"Prod" : "Friday"}, 
 #   "DC19" : {"Prod" : "Friday"}, 
}
TZ = {
    "DC17" : "21744",
    "DC4" : "21744",
    "DC2" : "21745",
    "DC8" : "21744",
    "DC10" : "21746",
    "DC12" : "21745",
    "DC15" : "21747",
    "DC18" : "21748",
    "DC19" : "21749",
}
DC_NAME = {
    "DC17" : "Toronto1",
    "DC4" : "Chandler1",
    "DC2" : "Amsterdam2",
    "DC8" : "Ashburn1",
    "DC10" : "Sydney1",
    "DC12" : "Rot1",
    "DC15" : "Shanghai1",
    "DC18" : "Moscow1",
    "DC19" : "Sao Paulo1",
}
for key,value in DC.items():
    actual_dc=key
    for key1,value1 in value.items():
        actual_env=key1
        actual_day=value1
        time_Zone=TZ[key]
        dc_value=DC_NAME[key]
        dc_total=key+' - '+dc_value
        smry="JAM "+dc_total + actual_env + " | Update Jam to R"+str(patch_no)
        descript="JAM "+dc_total + actual_env + " | Update Jam to R"+str(patch_no)
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
                    
        if actual_day is "Friday":
            actual_date = date
        else:
            actual_date = next_date
        if actual_env is "Prod":
            env_type = '11668'
        elif actual_env is "Sales":
            env_type = '11930'
        elif actual_env is "Developer":
            env_type = '11668'
        values = {
            'project' : 'CMSD', 
            'issuetype' : 'Change Request', # issue type
            'customfield_16584' : { 'value' : 'Low' }, # Priority 
            'summary' : smry, # summary
            'customfield_17680' : { 'value' : 'Low' }, # complexity of change
            'customfield_17681' : { 'value' : 'Low' }, # Pre-Testing
            'customfield_17682' : { 'value' : 'Low' }, # Scope of Validation
            'customfield_17683' : { 'value' : 'Low' }, # Rollback Plan
            'customfield_17684' : { 'value' : 'Low' }, # Customer landscape impact
            'customfield_16583' : {'value':'App', 'child': {'value':'Update/Upgrade'}}, # Category(s) 
            'components' : [{'name': 'JAM'}], #Components
            'customfield_15282' : {'value':'No Data Protection Regulation'}, # Customer Data Protection
            'customfield_10802' : { 'value' : dc_total }, # Data Center
            'customfield_16590' : { 'id' : time_Zone },# DC Time Zone
            'customfield_10842' : { 'id' : env_type }, # Environment Type 
            'customfield_16794' : {'value':'None'}, # Customer Impact
            'customfield_17055' : {'value':'No'}, # CCM Notify
            'customfield_17056' : { 'value' : 'Not Required' }, # Maintenance Page Required?
            'customfield_17057' : { 'value' : 'No' }, # Pop up enable required?
            'customfield_16814' : actual_date+ 'T11:30:00.000-0700', # requested Start 
            'customfield_16815' : actual_date+ 'T11:30:00.000-0700', # requested End 
            'description' : descript, # description
            'customfield_17426' : test_details, # Pre-Test Details
            'customfield_17427' : justification, # Business Justification
            'customfield_17058' : imp_steps, # Implementation Steps
            'customfield_16800' : back_steps, # Backout Steps
            'customfield_16801' : validate, # Validation Steps
            'customfield_16802' : { 'name' : 'svishwanath' }, # Validator
            'customfield_17059' : [{ 'value' : 'TechOwn - JAM' }],  #Tech Approver 17059
            'customfield_17060' : [{ 'value' : 'BusOwn - JAM' }], # Impact/Impl Approver 17060
                    }
        new_issue = jira.create_issue(fields=values)
        jira.assign_issue(new_issue, 'sureshkumara')
        print new_issue.key
