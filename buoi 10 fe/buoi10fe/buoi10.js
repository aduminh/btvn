const title=document.getElementById("title")
const allPtags=document.getElementsByTagName("p")
const redBg=document.getElementsByClassName("red-bg")
console.log(title.innerText)
console.log(allPtags[1].className)
console.log(redBg)
// let imgs=[
//     https://cdn.akamai.steamstatic.com/steam/apps/892970/header_292x136.jpg?t=1617258628;
//     https://cdn.akamai.steamstatic.com/steam/apps/739630/header_292x136.jpg?t=1613740031;
//     https://cdn.akamai.steamstatic.com/steam/apps/1105670/header_292x136.jpg?t=1623079449;
//     https://cdn.akamai.steamstatic.com/steam/apps/1097150/header_292x136.jpg?t=1621939955;

// ]
function changeImage(){
    currentIndex +=1;
    if (currentIndex>=Image.length){
        currentIndex=0

    }
    gallery.src=imgs[currentIndex]
}