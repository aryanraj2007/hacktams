var body = {
    'apps': [
      {
        'app': 1,
        'revision': 57
      },
      {
        'app': 1001,
        'revision': 22
      }
    ],
    'revert': true
  };
  
  kintone.api(kintone.api.url('/k/v1/preview/app/deploy.json', true), 'POST', body, function(resp) {
    // success
    console.log(resp);
  }, function(error) {
    // error
    console.log(error);
  });