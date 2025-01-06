// Student Registration System
const studentForm = document.getElementById('studentForm');
const studentTableBody = document.querySelector('#studentTable tbody');
const searchButton = document.getElementById('searchButton');
const searchType = document.getElementById('searchType');
const searchInput = document.getElementById('searchInput');
const searchResult = document.getElementById('searchResult');

let students = {};

// Add Student
studentForm.addEventListener('submit', (e) => {
  e.preventDefault();

  const enrollmentNo = document.getElementById('studentEnrollmentNo').value;
  const name = document.getElementById('studentName').value;
  const age = document.getElementById('studentAge').value;
  const course = document.getElementById('studentCourse').value;

  if (!course) {
    alert('Please select a course!');
    return;
  }

  if (students[enrollmentNo]) {
    alert('Student Enrollment Number already exists!');
    return;
  }

  students[enrollmentNo] = { name, age, course };
  displayStudents();

  studentForm.reset();
});

// Display Students
function displayStudents() {
  studentTableBody.innerHTML = '';
  for (const [enrollmentNo, details] of Object.entries(students)) {
    const row = `
      <tr>
        <td>${enrollmentNo}</td>
        <td>${details.name}</td>
        <td>${details.age}</td>
        <td>${details.course}</td>
        <td class="actions">
          <button class="edit" onclick="editStudent('${enrollmentNo}')">Edit</button>
          <button class="delete" onclick="deleteStudent('${enrollmentNo}')">Delete</button>
        </td>
      </tr>
    `;
    studentTableBody.insertAdjacentHTML('beforeend', row);
  }
}

// Edit Student
function editStudent(enrollmentNo) {
  const student = students[enrollmentNo];
  document.getElementById('studentEnrollmentNo').value = enrollmentNo;
  document.getElementById('studentName').value = student.name;
  document.getElementById('studentAge').value = student.age;
  document.getElementById('studentCourse').value = student.course;

  deleteStudent(enrollmentNo);
}

// Delete Student
function deleteStudent(enrollmentNo) {
  delete students[enrollmentNo];
  displayStudents();
}

// Search Student
searchButton.addEventListener('click', () => {
  const query = searchInput.value.toLowerCase();
  const type = searchType.value;
  let found = false;

  searchResult.style.display = 'none';

  if (!query) {
    alert('Please enter a search term!');
    return;
  }

  for (const [enrollmentNo, details] of Object.entries(students)) {
    if (
      (type === 'enrollment' && enrollmentNo.toLowerCase() === query) ||
      (type === 'name' && details.name.toLowerCase() === query)
    ) {
      searchResult.style.display = 'block';
      searchResult.className = '';
      searchResult.innerHTML = `
        <p><strong>Enrollment No:</strong> ${enrollmentNo}</p>
        <p><strong>Name:</strong> ${details.name}</p>
        <p><strong>Age:</strong> ${details.age}</p>
        <p><strong>Course:</strong> ${details.course}</p>
      `;
      found = true;
      break;
    }
  }

  if (!found) {
    searchResult.style.display = 'block';
    searchResult.className = 'error';
    searchResult.textContent = 'No student found matching the search criteria.';
  }
});
