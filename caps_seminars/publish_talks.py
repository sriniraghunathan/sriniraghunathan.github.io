def make_talk_line(opline, talk_date_arr, talk_time_arr, talk_location_arr, speaker_name_arr, speaker_affiliation_arr, talk_title_arr, talk_abstract_arr, speaker_image_arr, speaker_link_arr, speaker_email_arr, talk_link_arr):
    upcoming_written, past_written = False, False
    for (talk_date, talk_time, talk_location, speaker_name, speaker_affiliation, talk_title, talk_abstract, speaker_image, speaker_link, speaker_email, talk_link) in \
        zip(talk_date_arr, talk_time_arr, talk_location_arr, speaker_name_arr, speaker_affiliation_arr, talk_title_arr, talk_abstract_arr, speaker_image_arr, speaker_link_arr, speaker_email_arr, talk_link_arr):
            today = int( str(datetime.date.today()).replace('-','') )
            if int(talk_date)>=today and not upcoming_written:
                opline='%s\n' %(opline)
                opline='%s<tr><td colspan=6><font class="font_table_title"><i>Upcoming</i></font></td></tr>\n' %(opline)
                upcoming_written = True
            elif int(talk_date)<today and not past_written:
                opline='%s\n' %(opline)
                opline='%s<tr><td colspan=6><font class="font_table_title"><i>Past</i></font></td></tr>\n' %(opline)
                past_written = True
            talk_yyyy, talk_mmm, talk_dd = talk_date[:4], talk_date[4:6], talk_date[6:]
            talk_month = month_dic[int(talk_mmm)]
            opline='%s\n' %(opline)
            opline='%s<tr>\n' %(opline)
            opline='%s<td>%s %s, %s</td>\n' %(opline, talk_month, talk_dd, talk_yyyy)
            opline='%s<td style="width:6%%">\n' %(opline)
            opline='%s<a href="%s" target="_blank"><img valign="top" src="images/speakers/%s" class="avatar"></a>\n' %(opline, speaker_link, speaker_image)
            opline='%s</td>\n' %(opline)
            opline='%s<td><font class="font_speaker"><a href="%s" target="_blank">%s</a></td>\n' %(opline, speaker_link, speaker_name)
            opline='%s<td>%s</td>\n' %(opline, speaker_affiliation)
            opline='%s<td>%s</td>\n' %(opline, talk_title)
            opline='%s<td>%s</td>\n' %(opline, talk_link) 
            opline='%s</tr>\n' %(opline)
            opline='%s\n' %(opline)

    return opline

################################################################################
################################################################################
################################################################################

import numpy as np, os, glob, sys, time, datetime


talk_details_fname = 'talk_details.txt'
website_template_fname = 'caps_seminars_template.html'
website_fname = website_template_fname.replace('_template', '')

#month details
month_dic = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

#open the talk database file to get details of the seminars
talk_details = np.loadtxt(talk_details_fname, delimiter='%%%', dtype='str')
talk_date_arr, talk_time_arr, talk_location_arr, speaker_name_arr, speaker_affiliation_arr, talk_title_arr, talk_abstract_arr, speaker_image_arr, speaker_link_arr, speaker_email_arr, talk_link_arr = talk_details.T

#first open the template file
website_template_lines = open(website_template_fname, 'r')

#write output lines and publish the CAPS seminar page
website = open(website_fname, 'w')
for lines in website_template_lines:
    website_opline = lines.strip()
    if website_opline == 'add-talk-details-here':
        website_opline = make_talk_line(website_opline, talk_date_arr, talk_time_arr, talk_location_arr, speaker_name_arr, speaker_affiliation_arr, talk_title_arr, talk_abstract_arr, speaker_image_arr, speaker_link_arr, speaker_email_arr, talk_link_arr)
        website_opline = website_opline.replace('add-talk-details-here', '')
    website.writelines('%s\n' %(website_opline))
website.close()




