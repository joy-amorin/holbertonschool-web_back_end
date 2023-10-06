export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const updatedStudents = studentList
    .filter((student) => student.location === city)
    .map((student) => {
      const studentgGrade = newGrades.find((grade) => grade.studentId === student.id
            && grade.city === city);
      if (studentgGrade) {
        return {
          ...student,
          grade: studentgGrade.grado,
        };
      }
      return {
        ...student,
        grade: 'N/A',
      };
    });

  return updatedStudents;
}
