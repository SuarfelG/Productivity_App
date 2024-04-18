const inputbar=document.getElementById("input_bar")
const Add_Task=document.getElementById("Add_Task")
const list_container=document.getElementById("list_container")
const counter=8
function Adder()
{
    
    if(inputbar.value === '')
    {
    alert("You Need To Add Some Tasks!");
    }
    else
    {

     let li=document.createElement("li");

     li.innerHTML=inputbar.value;

     list_container.appendChild(li);

     inputbar.value=''


     let span=document.createElement("span")

     span.innerHTML="\u00d7"
     
     li.appendChild(span)

    }
    

    savedata();


}
list_container.addEventListener("click",function (e)
{
    if(e.target.tagName=="LI")
    {
        e.target.classList.toggle("check")
        savedata();
    }
   else if(e.target.tagName=="SPAN")
    {
        e.target.parentElement.remove("checked")
        savedata();
    }
},true);

function savedata()
{
    localStorage.setItem("data",list_container.innerHTML);
}
function showtask()
{
    list_container.innerHTML=localStorage.getItem("data");
}

showtask();