function ListStudent() {
  const dumyData = [
    { id: 1, name: "sam", email: "sam@sam.com" },
    { id: 2, name: "john", email: "john@john.com" },
    { id: 3, name: "cain", email: "cain@john.com" },
  ];

  return (
    <div className=" h-full w-full flex items-center justify-between">
      <div className="relative overflow-x-auto shadow-md sm:rounded-lg w-full">
        <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="px-6 py-3">
                Id
              </th>
              <th scope="col" className="px-6 py-3">
                Name
              </th>
              <th scope="col" className="px-6 py-3">
                Email
              </th>
            </tr>
          </thead>
          <tbody>
            {dumyData.map((item, index) => {
              return (
                <tr
                  className="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 border-gray-200"
                  key={item.id}
                >
                  <td class="px-6 py-4">{item.id}</td>
                  <td class="px-6 py-4">{item.name}</td>
                  <td class="px-6 py-4">{item.email}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );

}

export default ListStudent;