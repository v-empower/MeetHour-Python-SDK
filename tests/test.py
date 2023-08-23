import pymeethour.type.LoginType as LoginType
import pymeethour.type.AddContactType as AddContactType
import pymeethour.type.ContactsType as ContactsType
import pymeethour.type.EditContactType as EditContactType
import pymeethour.type.EditMeetingType as EditMeetingType
import pymeethour.type.GenerateJwtType as GenerateJwtType
import pymeethour.type.ScheduleMeetingType as ScheduleMeetingType
import pymeethour.type.CompletedMeetingsType as CompletedMeetingsType
import pymeethour.type.MissedMeeting as MissedMeeting
import pymeethour.type.ArchiveMeeting as ArchiveMeeting
import pymeethour.type.UpcomingMeetings as UpcomingMeetings
import pymeethour.type.ViewMeetings as ViewMeetings
import pymeethour.type.RecordingsList as RecordingsList
import pymeethour.type.RefreshToken as RefreshToken
import pymeethour.services.apiServices as apiServices
import pymeethour.type.time_zone as time_zone
import pymeethour.type.user_details as user_details


login_object = LoginType.LoginType('CLIENT_ID','CLIENT_SECRET','API_KEY','EMAIL','PASSWORD') # repalce details with the your own developer's details
apiservice = apiServices.MHApiService()
response = apiservice.login(login_object)
token = response.get('access_token')  
print(token)

add_contact_object = AddContactType.AddContactType("EMAIL","Fristname","lastname","phone","country_code ","Image","1")  # repalce contact details with the new contact details you want to add
apiservice = apiServices.MHApiService()
response = apiservice.add_contact(token, add_contact_object)
print(response)

contacts_object= ContactsType.ContactsType(0, 0,0)
apiservice = apiServices.MHApiService()
response = apiservice.contacts(token, contacts_object)
print(response)

edit_contact_object= EditContactType.EditContactType("id","countrycode","EMAIL", "Firstname","lastname","Image","1","phone") # repalce contact details with the new contact details you want to add
apiservice = apiServices.MHApiService()
response = apiservice.edit_contact(token, edit_contact_object)
print(response)

generate_jwt_object= GenerateJwtType.GenerateJwt("meeting_id","contact_id") #replace the meeting_id and conract_id with your details
apiservice = apiServices.MHApiService()
response = apiservice.generate_jwt(token, generate_jwt_object)
print(response)

edit_meeting_object= EditMeetingType.EditMeeting('meeting_id') #replace the meeting_id with the valid meeting_id
apiservice = apiServices.MHApiService()
response = apiservice.edit_meeting(token, edit_meeting_object)
print(response)

schedule_meeting_object= ScheduleMeetingType.ScheduleMeeting( )
apiservice = apiServices.MHApiService()
response = apiservice.schedule_meeting(token, schedule_meeting_object)
print(response)

completed_meetings_object= CompletedMeetingsType.CompletedMeetings()
apiservice = apiServices.MHApiService()
response = apiservice.completed_meetings(token, completed_meetings_object)
print(response)

missed_meetings_object= MissedMeeting.MissedMeetings()
apiservice = apiServices.MHApiService()
response = apiservice.missed_meetings(token, missed_meetings_object)
print(response)

archive_meetings_object= ArchiveMeeting.ArchiveMeetings("id")   #replace the id with that vaild id which can be found in the user_contact_details
apiservice = apiServices.MHApiService()
response = apiservice.archive_meetings(token, archive_meetings_object)
print(response)
  
upcoming_meetings_object= UpcomingMeetings.UpcomingMeetings()
apiservice = apiServices.MHApiService()
response = apiservice.upcoming_meetings(token, upcoming_meetings_object)
print(response)

view_meetings_object= ViewMeetings.ViewMeeting('meeting_id') #repace with your meeting_id
apiservice = apiServices.MHApiService()
response = apiservice.view_meetings(token, view_meetings_object)
print(response)

recordings_list_object= RecordingsList.RecordingsList('Local') # 'Dropbox'/'Local'/'Custom'
apiservice = apiServices.MHApiService()
response = apiservice.recordings_list(token, recordings_list_object)
print(response)


refresh_token_object= RefreshToken.RefreshToken('refresh_token','CLIENT_ID','CLIENT_SECRET','access_token') # replace the CLIENT_ID,CLIENT_SECRET,access_token with vaild details
apiservice = apiServices.MHApiService()
response = apiservice.refresh_token(token, refresh_token_object)
print(response)

time_zone_object= time_zone.time_zone(0,0,0) 
apiservice = apiServices.MHApiService()
response = apiservice.time_zone(token, time_zone_object)
print(response)

user_details_object= user_details.user_details(0,0,0,0) 
apiservice = apiServices.MHApiService()
response = apiservice.user_details(token, user_details_object)
print(response)  
