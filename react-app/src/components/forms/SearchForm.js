import React, {useState} from "react";
import { Container, FormGroup, Form, Label, Input, Col, Row, Button } from "reactstrap"

function SearchForm(){
  const [formData, setFormData] = useState({
    zipCode: '',
  });

  //handle initial search and reset pagecount for pagination. 
  async function handleSubmit(evt) {
    evt.preventDefault();    
    let zipCode = +formData.zipCode 
    let validate = await searchValidate(zipCode)
    
    if(validate === true){
      console.log("Valild!")
    }
  }

  //form validation
  async function searchValidate(zipcode) {
    if(zipcode){
      console.log(zipcode)
      return true;
    }
  }

  //Update form data
  function handleChange(evt) {
    evt.preventDefault()
    const { name, value } = evt.target;
    setFormData(l => ({ ...l, [name]: value }));
  }

  return (  
      <Container className="container-fluid ml-auto col-lg-6">
        <Form onSubmit={handleSubmit}>
          <Row>
          <FormGroup row className="mb-2 mr-sm-2 mb-sm-0 col-lg-3">
            <Label for="minPrice" className="mr-sm-2">
              Zip code:
            </Label>
            <Col sm={12}>
              <Input
                name="zipCode"
                pattern="[0-9]*"
                className="form-control"
                value={formData.zipCode}
                onChange={handleChange}
                autoComplete="zipCode"
                default="0"
                placeholder="0"
              />
            </Col>
          </FormGroup>
          <div className="d-grid gap-2 mt-2 mb-2">
            <Button className="bg-primary ml-auto col-lg-2 text-black" size="md" onSubmit={handleSubmit} >
              Search
            </Button>
          </div>
          </Row>
        </Form>
    </Container>   
  )
}

export default SearchForm;
