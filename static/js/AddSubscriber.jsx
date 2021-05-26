
function Subscribe(props){
  const [username, setUsername] = React.useState(null);
  //const [melon_name, setMelonname] = React.useState(null);
  const [password, setPassword] = React.useState(null);
  const [email, setEmail] = React.useState(null);
  const [phone, setPhone] = React.useState(null);
  

  function handleSubmit(evt){
    evt.preventDefault();
    console.log(username, email, phone, password);
    fetch('/api/subscribe', // THIS IS THE ROUTE WHERE YOU WILL HANDLE THE FORM ON YOUR SERVER
      {method: 'POST', 
      body: JSON.stringify({'name': username, 'password': password, 'email': email, 'phone': phone}), // ON THE SERVER YOU WILL GET THESE VALUES USING request.json.get 
      headers: {'Content-type': 'application/json'} //needed so the server knows where to get the values out from
      })
    .then(response => response.json())
    .then(data => {
      console.log(data);
        alert(data.status);
    })
  }

  return (
    <form onSubmit={(evt) => {handleSubmit(evt)}}>
      <h5>Subscribe to new melon notifications!</h5>
      <div>
      <label for="name">Enter your name</label>
      <br/>
      <input required name="name" type="text" onChange={ evt => { setUsername(evt.target.value) } }></input>
      </div>

      <div>
      <label for="password">Enter your password</label>
      <br/>
      <input required name="password" type="password" onChange={ evt => { setPassword(evt.target.value) } }></input>
      </div>

      <div>
      <label for="email">Enter your email address</label>
      <br/>
      <input required name="email" type="email" onChange={ evt => { setEmail(evt.target.value) } }></input>
      </div>

      <div>
      <label for="phone">Enter your phone number</label>
      <br/>
      
      <input required name="phone"  onChange={ evt => { setPhone(evt.target.value) } }></input>
      </div>
      
      <div>
      <input type='submit' />
      </div>
    </form>
    )
}
//pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" type="tel"
//<small>(Format: 123-456-7890)</small>
//<br/>
//<div>
      //<label for="melon_name">Enter name of melon you prefer</label>
      //<br/>
      
      //<input required name="melon_name"  onChange={ evt => { setMelonname(evt.target.value) } }></input>
      //</div>