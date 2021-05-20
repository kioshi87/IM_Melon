function Homepage(props) {
  return (
    <div id="home-banner" className="row">
      <div className="col">
        <h1>Ubermelon</h1>
        <p className="lead">Melons on demand.</p>
      </div>
    </div>
  );
}

function PageContainer(props) {
  const { children, className, title, ...rest } = props;
  return (
    <ReactRouterDOM.BrowserRouter>
      <h1>{title}</h1>
      <div {...rest} className={`row ${className || ""}`}>
        {children}
      </div>
    </ReactRouterDOM.BrowserRouter>
  );
}

function AllMelonsPage(props) {
  const { melons, addMelonToCart } = props;
  const melonCards = [];

  for (const melon of Object.values(melons)) {
    const melonCard = (
      <MelonCard
        key={melon.melon_code}
        code={melon.melon_code}
        name={melon.name}
        imgUrl={melon.image_url}
        price={melon.price}
        handleAddToCart={addMelonToCart}
      />
    );

    melonCards.push(melonCard);
  }

  return (
    <PageContainer title="All Melons" id="shopping">
      <div className="col-12 col-md-9 d-flex flex-wrap">{melonCards}</div>
    </PageContainer>
  );
}


function Navbar(props) {
  const { logo, brand, children, className } = props;

  const navLinks = children.map((el, i) => {
    return (
      <div key={i} className="nav-item">
        {el}
      </div>
    );
  });

  return (
    <nav className={`navbar ${className || ""}`}>
      <ReactRouterDOM.Link
        to="/"
        className="havbar-brand d-flex justify-content-center"
      >
        <img src={logo} height="30" />
        <span>{brand}</span>
      </ReactRouterDOM.Link>

      <section className="d-flex justify-content-center">{navLinks}</section>
    </nav>
  );
}

function MelonCard(props) {
  const { code, name, imgUrl, price, handleAddToCart } = props;

  return (
    <div className="card melon-card">
      <ReactRouterDOM.Link to={`/shop/${code}`}>
        <img src={imgUrl} className="card-img-top" />
      </ReactRouterDOM.Link>
      <div className="card-body">
        <h5 className="card-title">
          <ReactRouterDOM.Link to={`/shop/${code}`}>{name}</ReactRouterDOM.Link>
        </h5>
      </div>
      <div className="card-body pt-0 container-fluid">
        <div className="row">
          <div className="col-12 col-lg-6">
            <span className="lead price d-inline-block">
              ${price.toFixed(2)}
            </span>
          </div>
          <div className="col-12 col-lg-6">
            <button
              className="btn btn-sm btn-success d-inline-block"
              onClick={() => handleAddToCart(code)}
            >
              Add to cart
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}


