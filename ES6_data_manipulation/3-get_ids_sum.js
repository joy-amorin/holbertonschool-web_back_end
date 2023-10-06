export default function getStudentIdsSum(studentsList) {
  const initilalValue = 0;

  const sumValue = studentsList.reduce((accumulator, student) => accumulator + student.id,
    initilalValue);

  return sumValue;
}
