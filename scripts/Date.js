var day="";
var month="";
var myweekday="";
var year="";
mydate = new Date();
myday = mydate.getDay();
mymonth = mydate.getMonth();
myweekday= mydate.getDate();
weekday= myweekday;
myyear= mydate.getFullYear();

if(myday == 0)
day = " Sunday"      
else if(myday == 1)
day = " Monday"
else if(myday == 2)
day = " Tuesday"   
else if(myday == 3)
day = " Wednesday"   
else if(myday == 4)
day = " Thursday"
else if(myday == 5)
day = " Friday"
else if(myday == 6)
day = " Saturday"
if(mymonth == 0) {
month = "Jan"}
else if(mymonth ==1)
month = "Feb"
else if(mymonth ==2)
month = "Mar"
else if(mymonth ==3)
month = "Apr"
else if(mymonth ==4)
month = "May"
else if(mymonth ==5)
month = "Jun"
else if(mymonth ==6)
month = "Jul"
else if(mymonth ==7)
month = "Aug"
else if(mymonth ==8)
month = "Sep"
else if(mymonth ==9)
month = "Oct"
else if(mymonth ==10)
month = "Nov"
else if(mymonth ==11)
month = "Dec"

document.write(day + ", ");
document.write(myweekday + " " + month + " " + myyear + "");
