import axios from 'axios';

export default{

  data: {
    base_url: 'http://24.138.161.30:5000',
  },

  getHeaders () {
    return {
      headers: { Authorization: "Bearer ".concat(localStorage.getItem('jwtAuth'))}
    }
  },
  getRequest (end_point, callback, error_callback=null) {
    console.log(this.getHeaders());
      axios.get(this.data.base_url + end_point, this.getHeaders()).then(response => {
        callback(response)
      }).catch(e => {
        if (!error_callback) {
          // this.errors.push(e)
          console.log('request failed');
          console.log(e);
        } else {
          error_callback(e)
        }

      })
  },
  putRequest (end_point, payload, callback, error_callback=null) {
    axios.put(this.data.base_url + end_point, payload, this.getHeaders()).then(response => {
      callback(response)
    }).catch(e => {
      if (!error_callback) {
        // this.errors.push(e)
        console.log('request failed');
        console.log(e);
      } else {
        error_callback(e)
      }
    })
  },
  postRequest (end_point, payload, callback, error_callback=null) {
    axios.post(this.data.base_url + end_point, payload, this.getHeaders()).then(response => {
      callback(response)
    }).catch(e => {
      if (!error_callback) {
        // this.errors.push(e)
        console.log('request failed');
        console.log(e);
      } else {
        error_callback(e)
      }
    })
  },
  deleteRequest (end_point, callback, error_callback=null) {
    axios.get(this.data.base_url + end_point, this.getHeaders()).then(response => {
      callback(response)
    }).catch(e => {
      if (!error_callback) {
        // this.errors.push(e)
        console.log('request failed');
        console.log(e);
      } else {
        error_callback(e)
      }
    })
  },

}
