import React, {Component} from 'react';

export default class FormateurList extends Component {

    constructor(props) {
      super(props);
      this.state = {
        formateurs : []
      }
    }

    componentDidMount() {
      let _this = this;
      fetch('http://localhost:8000/formateurs')
        .then(function(response){
          return response.json()
        }).then(function(json) {
            _this.setState({formateurs : json})
        }).catch(function(ex) {
            console.log('parsing failed', ex)
          });
          }


    render() {
        return (
            <div>
              <h1>Formateurs</h1>

              <ul className="formateurs">
                {this.state.formateurs.map( formateur => {
                  return <li key={formateur.id}><span>{formateur.prenom}</span>&nbsp;-&nbsp;<span>{formateur.nom}</span></li>
                })}
              </ul>
            </div>
        );
    }
}


/*

{this.props.map( formateur =>
  <li key={formateur.id}><span>{formateur.id}</span>&nbsp;-&nbsp;<span>{formateur.prenom}</span>&nbsp;-&nbsp;<span>{formateur.nom}</span></li>
) }
*/
