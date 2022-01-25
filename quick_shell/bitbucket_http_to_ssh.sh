# usage: cd <repo>; bash /PATH/bitbucket_http_to_ssh.sh

http_to_ssh(){
	echo ""
	echo "checking for $1..."

    REPO_URL=`git remote -v | grep -m1 "^$1" | sed -Ene's#.*(https://[^[:space:]]*).*#\1#p'`
    if [ -z "$REPO_URL" ]; then
	if [ "$1" == "upstream" ]; then
	    echo "-- No upstream found"
	    exit
	else
	    echo "-- ERROR:  Could not identify Repo url."
	    echo "   It is possible this repo is already using SSH instead of HTTPS."
	    exit
	fi
    fi

	if [[ "$REPO_URL" == *"src/master"* ]]; then
		USER=`echo $REPO_URL | sed -Ene's#https://bitbucket.org/([^/]*)/(.*)/src/master/#\1#p'`
	else
	    USER=`echo $REPO_URL | sed -Ene's#https://(.*)@bitbucket.org/([^/]*)/(.*).git#\2#p'`
	fi
    if [ -z "$USER" ]; then
		echo "-- ERROR:  Could not identify User."
		exit
    fi

	if [[ "$REPO_URL" == *"src/master"* ]]; then
    	REPO=`echo $REPO_URL | sed -Ene's#https://bitbucket.org/([^/]*)/(.*).git#\2#p'`
	else
	    REPO=`echo $REPO_URL | sed -Ene's#https://(.*)@bitbucket.org/([^/]*)/(.*).git#\3#p'`
	fi
    if [ -z "$REPO" ]; then
		echo "-- ERROR:  Could not identify Repo."
		exit
    fi

    NEW_URL="git@bitbucket.org:$USER/$REPO.git"
    echo "Changing repo url from "
    echo "  '$REPO_URL'"
    echo "      to "
    echo "  '$NEW_URL'"
    echo ""

    CHANGE_CMD="git remote set-url $1 $NEW_URL"
    echo "$CHANGE_CMD"
    `$CHANGE_CMD`
}

http_to_ssh "origin"
http_to_ssh "upstream"

echo "Success"
