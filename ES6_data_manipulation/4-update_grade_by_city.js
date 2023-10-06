export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList.map((student) => {
    const studentGrade = newGrades.find((grade) => grade.studentId === student.id
     && grade.city === city);
    if (studentGrade) {
      return {
        ...student,
        grade: studentGrade.grado,
      };
    }
    return {
      ...student,
      grade: 'N/A',
    };
  });
}
