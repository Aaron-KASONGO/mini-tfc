class App extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			dropped: false,
			onDrag: false,
			file: null
		}
	}

	onDragEnter = () => {
		console.log("Merci d'entrer");
		this.setState({
			onDrag: true
		})
	}

	onDragLeave = () => {
		console.log("Merci de sortir");
		this.setState({
			onDrag: false
		})
	}

	onDrop = (e) => {
		e.preventDefault();
		console.log(e.target.files[0]);
		this.setState({
			dropped: true,
			onDrag: false,
			file: e.target.files[0]
		});
	}

	onChange = (e) => {
		this.setState({
			dropped: true,
			file: e.target.files[0]
		})
	}

	onSend = (e) => {
		e.preventDefault();
		let data = new FormData();
		axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
		axios.defaults.xsrfCookieName = "csrftoken"

		console.log(this.state.file);

		data.append('file', this.state.file);

		axios.post('/', data, {
			headers: {
				'Content-Type': 'multipart/form-data'
			  }
		})
			.then(result => console.log(result))
			.catch(errors => console.log(errors))
	}

    render() {
        return (
			<div className="container">
				<div className="row align-items-center vh-100">
					<div className="col-12 col-md-6 offset-md-3">
						<div className="card shadow-sm border-blue-color">
						<div className="card-title text-center mt-2 text-muted">Analysez vos documents</div>
							{
								this.state.dropped ?
								<div className="d-flex flex-column justify-content-center align-items-center">
									<p>Merci d'avoir Uploadé !</p>
									<div>
										<button className="btn btn-primary" onClick={(e) => this.onSend(e)}>Analysez</button>
									</div>
								</div>
								:
								<div
									onDragEnter={() => this.onDragEnter()}
									onDragLeave={() => this.onDragLeave()}
									onDrop={(e) => this.onDrop(e)}
									className={this.state.onDrag ? "card-body d-flex justify-content-center m-3 border-dashed bg-blue text-muted dragover drag-enter" : "card-body d-flex justify-content-center m-3 border-dashed bg-blue text-muted dragover"}
								>
									<img src="static/img/Stuck at Home - To Do List.png" className="card-img img-fluid upload-img" alt="Upload image" />
									<input type="file" accept="application/pdf" name="file" id="file" className="position-absolute w-75 h-75 input-field" onChange={(e) => this.onChange(e)} />
								</div>
							}
							
						</div>
					</div>
				</div>
			</div>
        )
    }
}


ReactDOM.createRoot(document.getElementById("root")).render(<App />)