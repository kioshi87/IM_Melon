function Admin(props){
    const [melonName, setMelonName] = React.useState(0);
    const [melonQty, setMelonQty] = React.useState(0);
    const [melonType, setMelonType] = React.useState(0);
    const [melonSeason, setMelonSeason] = React.useState(0);

    function handleSubmit(evt){
      evt.preventDefault();
      console.log(melonName, melonQty, melonType, melonSeason);
      fetch('/api/add_melon', // THIS IS THE ROUTE WHERE YOU WILL HANDLE THE FORM ON YOUR SERVER
        {method: 'POST', 
        body: JSON.stringify({'name': melonName, 'quantity': melonQty, 'type': melonType, 'season': melonSeason}), // ON THE SERVER YOU WILL GET THESE VALUES USING request.json.get 
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
        <h5>Enter Melon Updates</h5>
        <div>
        <label for="melonName">Melon Name</label>
        <br/>
        <input required name="melonName" type="text" onChange={ evt => { setMelonName(evt.target.value) } }></input>
        </div>

        <div>
        <label for="melonQty">Melon Quantity</label>
        <br/>
        <input required name="melonQty" type="number" onChange={ evt => { setMelonQty(evt.target.value) } }></input>
        </div>

        <div>
        <label for="melonType">Melon Type</label>
        <br/>
        <input required name="melonType" type="text" onChange={ evt => { setMelonType(evt.target.value) } }></input>
        </div>

        <div>
        <label for="melonSeason">Melon Season</label>
        <br/>
        <input required name="melonSeason" type="text" onChange={ evt => { setMelonSeason(evt.target.value) } }></input>
        </div>
        
        <div>
        <input type='submit' />
        </div>
      </form>
      )
  }
  //if (props.user === false) {
    //return <p>You must be logged in as admin to view this page.</p>
  //}