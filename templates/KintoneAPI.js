var body = {
    'app': 1,
    'properties': {
      'Text__single_line_1': {
        'type': 'SINGLE_LINE_TEXT',
        'code': 'Text__single_line_1',
        'label': 'Text (single-line)',
        'noLabel': false,
        'required': true,
        'unique': true,
        'maxLength': 64,
        'minLength': 0,
        'defaultValue': '',
        'expression': '',
        'hideExpression': false
      },
      'Number': {
        'type': 'NUMBER',
        'code': 'Number',
        'label': 'Number',
        'noLabel': true,
        'required': false,
        'unique': false,
        'maxValue': 64,
        'minValue': 0,
        'defaultValue': '12345',
        'digit': true,
        'displayScale': '',
        'expression': '',
        'unit': '$',
        'unitPosition': 'BEFORE'
      }
    }
  };
  
  kintone.api(kintone.api.url('/k/v1/preview/app/form/fields.json', true), 'POST', body, function(resp) {
    // success
    console.log(resp);
  }, function(error) {
    // error
    console.log(error);
  });