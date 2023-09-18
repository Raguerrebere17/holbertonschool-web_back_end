export default function createReportObject(employeesList) {
  const reportObject = {
    allEmployees: employeesList,
    getNumberOfDepartaments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
  return reportObject;
}
