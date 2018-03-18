/AWAY
    - User status is away, it should say it in the channel the user is to all users
    - /away [reason] shows the reason why the student is away
    - /away toggles the away state
    - You are no longer marked as being away
    - You have been marked as being away

/NICK
    - /NICK not enough parameters
    - Change nickname and change nickname in the status bar
    - Broadcast message == Eddy has changed nick to EddyMogollon

/WHOIS
    - /whois [name]
    - == No such nick/channel: Eddy == End of WHOIS
    - /WHOIS no nickname given
    - Displays information of user requested. Includes Full Name, Host, Channels User is in, and Oper Status

/RULES
    - [20:53] == End of RULES command.
        [20:53] == - webchat.SwiftIRC.net Server Rules -
        [20:53] == - Use of this IRC server is provided free of charge.  However,
        [20:53] == - you MUST agree to follow the SwiftIRC rules which can be read
        [20:53] == - at http://www.swiftirc.net/index.php?page=rules

        [20:53] == -
        [20:53] == End of RULES command.

/VERSION
    [21:01] == Unreal3.2.6.SwiftIRC(10). webchat.SwiftIRC.net FhiXeOoZEM3 [*=2309]
    [21:01] == NAMESX SAFELIST HCN MAXCHANNELS=50 CHANLIMIT=#:50 MAXLIST=b:100,e:100,I:100 NICKLEN=30 CHANNELLEN=32 TOPICLEN=307 KICKLEN=307 AWAYLEN=307 MAXTARGETS=20 WALLCHOPS are supported by this server
    [21:01] == WATCH=128 SILENCE=10 MODES=12 CHANTYPES=# PREFIX=(ohv)@%+ CHANMODES=beIqa,kfL,lj,psmntirRcOAQKVCuzNSMTGHFEB NETWORK=SwiftIRC CASEMAPPING=ascii EXTBAN=~,cqnrLT ELIST=MNUCT STATUSMSG=@%+ EXCEPTS INVEX are supported by this server
    [21:01] == CMDS=KNOCK,MAP,DCCALLOW,USERIP are supported by this server
    Shows you the version of the IRCd and other
    info related to it. If you specify a server, you
    will be shown information relating to that server

/QUIT
    quit [reason] SwiftIRC559 [~qwebirc@Swift-BF629A56.hsd1.fl.comcast.net] has quit [Quit: **** yall]

/INFO
    [21:05] == IRC --
    [21:05] == Based on the original code written by Jarkko Oikarinen
    [21:05] == Copyright (c) 1996-2001 Hybrid Development Team

    [21:05] ==
    [21:05] == This program is free software; you can redistribute it and/or
    [21:05] == modify it unde[21:19] == INVITE Not enough parameters
    [21:23] == minombre No such channel
    [21:23] == Eddy #minombrer the terms of the GNU General Public License as
    [21:05] == published by the Free Software Foundation; either version 2, or
    [21:05] == (at your option) any later version.
    [21:05] ==
    [21:05] == Birth Date: Thu Sep 22 2016 at 20:50:15 UTC, compile # 1
    [21:05] == On-line since Fri Oct 7 23:20:15 2016
    [21:05] == End of /INFO list.

/JOIN
    channels should start with #
    [21:30] Channel names begin with # (corrected automatically).

/INVITE
    INVITE <nickname> <channel>
    [21:19] == INVITE Not enough parameters
    [21:23] == minombre No such channel
    [21:23] == Eddy #minombre

/RESTART
    == Permission Denied - You're not an IRC operator
    
/USERHOST
    - /userhost [user] [user] ...
    [21:57] == Iann=+4c6e04df@gateway/web/freenode/ip.76.110.4.223 
    [21:57] == Eddy=+4c6e04df@76.110.4.223[21:57] 
    ==
    
/USERS
    [22:07] == 605 1527 Current local users 605, max 1527
    [22:07] == 84209 97718 Current global users 84209, max 97718
    
/PRIVMSG
    [22:18] *#yosoy* yooyoy
    [22:18] == Cannot send to channel: #yosoy
    [22:17] *minombre* yooyoy
    [22:17] == No such nick/channel: minombre
    [22:16] *Iann* helllo
    [22:16] *Iann* helllo
    PRIVMSG <msgtarget> <message>
    
/PART
    PART <channels> [<message>]
    [22:49] == #minombre You're not on that channel
    [22:49] == Eddy [4c6e04df@gateway/web/freenode/ip.76.110.4.223] has left #minombre []
    [22:50] == Eddy [4c6e04df@gateway/web/freenode/ip.76.110.4.223] has joined #minombre
    [22:50] == Eddy [4c6e04df@gateway/web/freenode/ip.76.110.4.223] has left #minombre ["me voy par carajo"]
    [22:51] == Eddy [4c6e04df@gateway/web/freenode/ip.76.110.4.223] has joined #minombre

/NOTICE
    [22:56] [notice(Iann)] Hello
    [22:56] [notice(Iann)] Hello
    