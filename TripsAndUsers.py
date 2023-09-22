# The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.
# Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.
# Return the result table in any order.

import pandas as pd 

def trips_and_users(trips, users):
    df = trips.merge(users, left_on='client_id', right_on='users_id').merge(users, left_on='driver_id', right_on='users_id', suffixes=('_client', '_driver'))
    df = df[(df['banned_client'] == "No") & (df['banned_driver'] == "No") & (df['request_at'] >= "2013-10-01") & (df['request_at'] <= "2013-10-03")]

    if len(df) == 0: 
        return pd.DataFrame(columns=['Day','Cancellation Rate'])
    
    df = round(df.groupby(by='request_at').apply(lambda x: ((x['status'] == 'cancelled_by_client') | (x['status'] == 'cancelled_by_driver')).sum()) / df.groupby(by="request_at")['status'].count(), 2).reset_index(name='Cancellation Rate')
    return df.rename(columns={'request_at': 'Day'})
    
# schema 
data = [['1', '1', '10', '1', 'completed', '2013-10-01'], ['2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'], ['3', '3', '12', '6', 'completed', '2013-10-01'], ['4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'], ['5', '1', '10', '1', 'completed', '2013-10-02'], ['6', '2', '11', '6', 'completed', '2013-10-02'], ['7', '3', '12', '6', 'completed', '2013-10-02'], ['8', '2', '12', '12', 'completed', '2013-10-03'], ['9', '3', '10', '12', 'completed', '2013-10-03'], ['10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03']]
Trips = pd.DataFrame(data, columns=['id', 'client_id', 'driver_id', 'city_id', 'status', 'request_at']).astype({'id':'Int64', 'client_id':'Int64', 'driver_id':'Int64', 'city_id':'Int64', 'status':'object', 'request_at':'object'})

data = [['1', 'No', 'client'], ['2', 'Yes', 'client'], ['3', 'No', 'client'], ['4', 'No', 'client'], ['10', 'No', 'driver'], ['11', 'No', 'driver'], ['12', 'No', 'driver'], ['13', 'No', 'driver']]
Users = pd.DataFrame(data, columns=['users_id', 'banned', 'role']).astype({'users_id':'Int64', 'banned':'object', 'role':'object'})
print(trips_and_users(Trips, Users))