window.onload=function() {watch()};
function watch(){
    var btn= document.getElementById('btnStop');
    btnDisabled(btn);
}
function rollForTurn(){
    var xArray=[];
    var ranNum="";
    var minimum=1;
    var maximum = 11;
    var first="";
    var txt1="";
    for(var i=0; i<2; i++){
        ranNum=Math.floor(Math.random()* (maximum - minimum)+minimum);
        xArray.push(ranNum);
    }
    diceRoll();
    for(i=0; i<xArray.length;i++){
        var result= 1+1;
        var pOne=xArray[0];
        var pTwo= xArray[1];
        if(pOne==pTwo){
            pOne=1;
            pTwo=2;
        }
        txt1="Player 1 rolled ["+pOne+"]<br>";
        writeMsg(txt1);
        txt1= txt1+ "Player 2 rolled ["+pTwo+"]<br><br>"
        setTimeout(function() {writeMsg(txt1);},1000);
    }
    if(pOne>pTwo){
        first="Player 1";
        setTimeout(function(){txt1 = txt1 + "Player 1 wins, please choose a square.";},2000);
        setTimeout(function(){writeMsg(txt1);},2000);
    }
    else if(pOne<pTwo){
        first="Player 2";
        setTimeout(function(){txt1 = txt1 + "Player 2 wins, please choose a square.";},2000);
        setTimeout(function(){writeMsg(txt1);},2000);
    }
    return first;
}
function startGame(){
    var xturn= 0;
    activePlayer= rollForTurn();
    if (activePlayer ==""){
        activePlayer=rollForTurn();
    }
    setTimeout(function(){hideGameMsg();}, 4000);
    var btn =document.getElementById("btnStart");
    btnDisabled(btn);
    var btn = document.getElementById("btnStop");
    stopEnabled(btn);

    var showPlayer= document.getElementById("showPlayer");
    showPlayer.innerHTML= activePlayer;
    showPlayer.style.color="green";
}
function btnDisabled(btn){
    BroadcastChannel.style.color="#fff";
    btn.style.border= "2px solid tgb(153,153,102)";
    btn.style.backgroundColor="rgb(214,214,194)";
    btn.btnDisabled=true;

}
function stopEnabled(btn){
    btn.style.color="#fff";
    btn.style.border= "2px solid rgb(204,0,0)";
    btn.style.backgroundColor="rgb(255,51,51)"
    btn.btnDisabled=false;
}
function startEnabled(btn){
    btn.style.color="#fff";
    btn.style.border="2px solid rgb(0,153,0)";
    btn.style.backgroundColor="rgb(57,230,0)";
    btn.btnDisabled=false;
}
function stopGame(){
    hideGameMsg();
    var btn= document.getElementById('btnStart');
    startEnabled(btn);
    var btn= document.getElementById("btnStop");
    btnDisabled(btn);
    var showPlayer= document.getElementById("showPlayer");
    showPlayer.innerHTML="Game Stopped";
    showPlayer.style.color="red";

    var arrayO= document.getElementsByClassName("O");
    var arrayX= document.getElementsByClassName("X");
    for(var i=0; i< arrayO.length; i++){
        arrayO[i].style.transform="translateY(-100%)";
    }
    for(var i=0; i< arrayX.length; i++){
        arrayX[i].style.transform="translateY(100%)";
    }
    document.getElementById("boardState").innerHTML="";
}
function showGameMsg(){
    document.getElementById("gameMsgBox").style.display="block";
}
function hideGameMsg(){
    clearMsg();
    document.getElementById("gameMsgBox").style.display="none";
}
function writeMsg(txt){
    showGameMsg();
    document.getElementById("gameMsg").innerHTML=txt;
}
function clearMsg(){
    document.getElementById("gameMsg").innerHTML=""
}
function saveSettings(){
    var p1Index= document.getElementById("player1").selectedIndex;
    var p1Selected= document.getElementById("player1").options;
    var p2Index= document.getElementById("player2").selectedIndex;
    var p2Selected= document.getElementById("player2").options;
    if(p1Selected[p1Index].text == p2Selected[p2Index].text){
        alert("Error - player 1 anf player 2 cannot both be assigned as: " + p1Selected[p1Selected.p1Index].text);
    } else{
        document.getElementById("p1Display").innerHTML=p1Selected[p1Index].text;
        document.getElementById("p2Display").innerHTML=p2Selected[p2Index].text;
    }
}
function getAvatars(){
    var p1Avatar= document.getElementById("p1Display").innerHTML;
    var p2Avatar= document.getElementById("p2Display").innerHTML;
    var avatarArray=[p1Avatar,p2Avatar];
    return avatarArray;

}
function determineAvatar(){
    var avatarArray= getAvatars();
    var active= document.getElementById("showPlayer").innerHTML;
    var p1Avatar= avatarArray[0];
    var p2Avatar= avatarArray[1];
    if (active== "Player 1"){
        var paintAvatar= p1Avatar;
    }else if(active =="Player 2")
    {
        var paintAvatar= p2Avatar;
    }
    return paintAvatar;
}
function avatarPlaced(){
    var parseTxt= document.getElementById("gameMsg").innerHTML;
    var showPlayer = document.getElementById("showPlayer");
    if (parseText == "That's three in a row, Player 1 wins!"|| parseText =="That's three in a row, Player 2 wins!"){
        showPlayer.innerHTML="Game Stopped";
        showPlayer.style.color="red";
    }
    activePlayer = showPlayer.innerHTML;
    if(activePlayer=="Player 1"){
        showPlayer.innerHTML = "Player 2";
    } else{
        showPlayer.innerHTML="Player 1";
    }
    check4Tie();
}
function check(info,square){
    for(var i in info){
        var tempInfo = info[i].charAt(0);
        if(tempInfo==square){
            return tempInfo;
        }
    }
}
function recordMoves(square){
    var proposedMove = square;
    var boardState= document.getElementById("boardState").innerHTML;
    var info= boardState.split(",");
    var verdict= check(info , square);
    return verdict;
}
function recordMove(currentMove){
    var target = document.getElementById("boardState");
    var previousMoves=target.innerHTML;
    target.innerHTML= previousMoves+currentMove;
}
function checkForWinCon(){
    var squareArray =[];
    var target= document.getElementById("boardState");
    var info = target.innerHTML;
    info=info.substring(1);
    info = info.split(,);
    info.sort();
    for (var i in info){
        squareArray.push(info[i].charAt(0));
    }
    checkWinCon1(info,squareArray);
    checkForWinCon2(info,squareArray);
}