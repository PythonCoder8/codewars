function likes(names) {
  let result = '';
  switch (true){
      case (names.length == 0):
        result = 'no one likes this';
        break;
      case (names.length == 1):
        result = `${names[0]} likes this`;
        break;
      case (names.length == 2):
        result = `${names[0]} and ${names[1]} like this`;
        break;
      case (names.length == 3):
        result = `${names[0]}, ${names[1]} and ${names[2]} like this`;
        break;
      case (names.length > 3):
        result = `${names[0]}, ${names[1]} and ${names.length - 2} others like this`;
        break;
  }
  return result
}
