# Depuis que Firefox a décidé, quelque part entre 2007 et 2009, de retirer la fonctionnalité dans l'historique d'accéder à la première visite d'un URL.
# exemple d'exécution en cmd : py -m first_visits google.com/

# https://support.mozilla.org/fr/questions/937585#answer-369869
# https://support.mozilla.org/fr/kb/profils-la-ou-firefox-conserve-donnees-utilisateur#w_trouver-son-profil

import os
import pandas as pd
import sqlite3
import sys

path = '\\'.join(os.getcwd().split('\\')[:3]) + '\AppData\Roaming\Mozilla\Firefox\Profiles\\'
db = path + os.listdir(path)[0] + '\\places.sqlite'
con = sqlite3.connect(db)
if len(sys.argv)>1:
    url = sys.argv[1]
else:
    url = 'google.com/'

script = f"""SELECT url, title, visit_count, datetime(first_visit/1000000,'unixepoch') AS EarliestVisit, datetime(last_visit_date/1000000,'unixepoch') AS LatestVisit
FROM moz_places INNER JOIN
    (SELECT place_id, MIN(visit_date) AS first_visit
    FROM moz_historyvisits
    GROUP BY place_id) AS FirstVisits
    ON FirstVisits.place_id = moz_places.id
WHERE url LIKE '%%{url}'
ORDER BY visit_count DESC"""

sql_query = pd.read_sql_query (script, con)
df = pd.DataFrame(sql_query, columns = ['url', 'title', 'visit_count', 'EarliestVisit', 'LatestVisit'])
print(df.to_string())