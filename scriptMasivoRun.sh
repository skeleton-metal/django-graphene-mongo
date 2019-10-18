MyPid=$(pgrep -f "/usr/bin/python3 manage.py ProcessMasivo")

if [ "$MyPid" != "" ];
    then
    echo "$MyPid corriendo"
else
    echo "$MyPid no corriendo"
    /usr/bin/python3 /appuser/proyectos/stock-api/manage.py ProcessMasivo
fi