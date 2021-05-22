function App() {
  const [melons, setMelons] = React.useState({});
  const [Cart, setCart] = React.useState({});
  
  return (
      <ReactRouterDOM.BrowserRouter>
      <div className="container-fluid">
        <ReactRouterDOM.Route exact path="/">
          <Homepage />
        </ReactRouterDOM.Route>
        <ReactRouterDOM.Route exact path="/login">
          {loading ? (
            <Loading />
          ) : (
            <AllMelonsPage melons={melons} addMelonToCart={addMelonToCart} />
          )}
        </ReactRouterDOM.Route>
        <ReactRouterDOM.Route exact path="/add_new_melon">
          {loading ? (
            <Loading />
          ) : (
            <ShoppingCartPage cart={Cart} melons={melons} />
          )}
        </ReactRouterDOM.Route>
      </div>
      </ReactRouterDOM.BrowserRouter>
  );
}

ReactDOM.render(<App />, document.querySelector("#root"));
