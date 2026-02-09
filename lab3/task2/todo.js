const form=document.getElementById('todo-form');
const input=document.getElementById('todo-input');
const list=document.getElementById('todo-list');

form.addEventListener('submit',(event)=>{
  event.preventDefault();
  const text=input.value.trim();
  if (text===''){
return;
}

  const listItem=document.createElement('li');
  const checkbox=document.createElement('input');
  checkbox.type='checkbox';

  const span=document.createElement('span');
  span.textContent=text;

  const deleteButton=document.createElement('button');
  deleteButton.textContent='Delete';

  checkbox.addEventListener('change',() =>{
    listItem.classList.toggle('done',checkbox.checked);
  });

  deleteButton.addEventListener('click',() =>{
    list.removeChild(listItem);
  });

  listItem.appendChild(checkbox);
  listItem.appendChild(span);
  listItem.appendChild(deleteButton);

  list.appendChild(listItem);
  input.value = '';
});