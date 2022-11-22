import pathlib
import time
import unittest
from backup import Backup
import info_handler as ih
import platform
import os
from filecmp import dircmp
from filecmp import cmpfiles
from datetime import datetime as date
import datenbank
import shutil

device_name = "testCases"
<<<<<<< HEAD

def are_dir_trees_equal(dir1, dir2):
    
    dirs_cmp = dircmp(dir1, dir2) 
    
    if len(dirs_cmp.left_only) > 0 or len(dirs_cmp.right_only) > 0 or len(dirs_cmp.funny_files) > 0: # überprüfen, ob unterschiedliche Files oder Dirs vom Namen her
                                                                                                     #existieren 
        return False                                                                                 
    
    (match, mismatch, errors) =  cmpfiles(dir1, dir2, dirs_cmp.common_files, shallow=False)
    
    if len(mismatch) > 0 or len(errors) > 0:    # nach in halt überprüfen
        return False
    
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not are_dir_trees_equal(new_dir1, new_dir2):
            return False
    return True


=======
>>>>>>> 50e2fc88de40f8147256936dce466876ccb925ae
class TestRestore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.daten = datenbank.Datenbank()
        cls.config = ih.get_json_info(device_name)
        cls.workingDirectory = str(pathlib.Path(__file__).parent.resolve())

        jewel_list = cls.config["jewel_sources"][device_name]
        i = 0
        for element in jewel_list:
            jewel_list[i] = cls.workingDirectory + element
            i= i+ 1

        cls.backup = Backup(jewel_list, cls.workingDirectory + "/" + cls.config["destination"][device_name], True)
<<<<<<< HEAD
        cls.backup.initialize_backup()
        #time.sleep(1)
=======
        cls.backup.initialize_backup(0)
        time.sleep(15)
>>>>>>> 50e2fc88de40f8147256936dce466876ccb925ae

    def test_a_restore_Jewel_only_Fullbackup(self):
        restoreDay = date.today()
        jewel = self.daten.get_restore_Jewel(restoreDay, 1)
        self.assertTrue(jewel!= None,"An answer is None")
        self.assertTrue(len(jewel.res_file) == 1,f"The lenght is incorrect. Should be 1, but is {len(jewel.res_file)}")
        self.assertTrue(jewel.jewel_id == 1, f"The id is wrong. Must be 1, but is {jewel.jewel_id}")
        self.assertTrue(jewel.res_file[0].file_name == 'test1.txt', 'Name is wrong')
        self.assertTrue(jewel.res_file[0].origin_location == f'{self.workingDirectory}/unitTestFiles/jewel/test1.txt', f'jewel path is wrong. Its {jewel.res_file[0].origin_location}')
        self.assertTrue(jewel.res_file[0].backup_location == f'{self.workingDirectory}/unitTestFiles/backupLocation/fullBackuptestCases/jewel/test1.txt', 'backup location is wrong')
        self.assertTrue(jewel.res_file[0].version_number == 1, f'Version Number is wrong. Should be 1, but is {jewel.res_file[0].version_number}')

    def test_b_restore_Jewel_date_in_past(self):
        restoreDay = date.today()
        restoreDay = restoreDay.replace(year=2000)
        jewel = self.daten.get_restore_Jewel(restoreDay,1)
        self.assertTrue(jewel== None,"The answer should be None")


    def test_c_restore_File_only_Fullbackup(self):
        restoreDay = date.today()
        jewel = self.daten.get_restore_File(restoreDay, f"testCases{self.workingDirectory}/unitTestFiles/jewel/test1.txt")
        self.assertTrue(jewel!= None,"An answer is None")

        self.assertTrue(jewel.res_file[0].file_name == 'test1.txt', f'Name is wrong, it returns {jewel.res_file[0].file_name}')
        self.assertTrue(jewel.res_file[0].origin_location == f'{self.workingDirectory}/unitTestFiles/jewel/test1.txt', f'jewel path is wrong: {jewel.res_file[0].origin_location}')
        self.assertTrue(jewel.res_file[0].backup_location == f'{self.workingDirectory}/unitTestFiles/backupLocation/fullBackuptestCases/jewel/test1.txt', 'backup location is wrong')

    def test_d_restore_jewel_diff_backup_change_file(self):
      restoreDay = date.today()
      file = open(f"{self.workingDirectory}/unitTestFiles/jewel/test1.txt", "a")
      for i in range(5):
          file.write("Change change change")
      file.close()
      #touch the the dir, for the real behavior of
      os.utime(f"{self.workingDirectory}/unitTestFiles/jewel")

    
<<<<<<< HEAD
      time.sleep(1)
      self.backup.initialize_backup()
      time.sleep(1)
=======
      time.sleep(10)
      self.backup.initialize_backup(0)
      time.sleep(30)
>>>>>>> 50e2fc88de40f8147256936dce466876ccb925ae
      jewel = self.daten.get_restore_Jewel(restoreDay,1)
      self.assertTrue(jewel.res_file[0].version_number == 2, f'Version Number is wrong. Should be 2, but is {jewel.res_file[0].version_number}')

   
    def test_e_restore_Jewel_diff_backup_new_file(self):
        restoreDay = date.today()
        #create_new_file
        file = open(os.path.join(os.path.dirname(__file__), "unitTestFiles/jewel/test_new.txt"), "a")

        for i in range(5):
            file.write("Hello World in test_new.txt\n")
        file.close()
<<<<<<< HEAD
        self.backup.initialize_backup()
        time.sleep(1)
=======
        self.backup.initialize_backup(0)
        time.sleep(45)
>>>>>>> 50e2fc88de40f8147256936dce466876ccb925ae
        jewel = self.daten.get_restore_Jewel(restoreDay,1)
        self.assertTrue(jewel!= None,"An answer is None")
        self.assertTrue(len(jewel.res_file) == 2,"The lenght is incorrect")


    def test_f_restore_File_diff_backup(self):
        restoreDay = date.today()
        jewel = self.daten.get_restore_File(restoreDay, f"testCases{self.workingDirectory}/unitTestFiles/jewel/test1.txt")
        self.assertTrue(jewel!= None,"An answer is None")
        self.assertTrue(jewel.res_file[0].version_number == 2, f"Version Number ist wrong, should be 2, is {jewel.res_file[0].version_number}")


    @classmethod
    def tearDownClass(cls):

        os.remove("datenbank.db")
        shutil.rmtree(cls.config["destination"][device_name])
        shutil.rmtree(cls.config["restore_destination"][device_name])
        os.remove("unitTestFiles/jewel/test_new.txt")


def suite():
  suite = unittest.TestSuite()

 

  suite.addTest(TestRestore.test_a_restore_Jewel_only_Fullbackup)
  suite.addTest(TestRestore.test_b_restore_Jewel_date_in_past)
  suite.addTest(TestRestore.test_c_restore_File_only_Fullbackup)
  suite.addTest(TestRestore.test_d_restore_jewel_diff_backup_change_file)
  suite.addTest(TestRestore.test_e_restore_Jewel_diff_backup_new_file)
  suite.addTest(TestRestore.test_f_restore_File_diff_backup)
  return suite

        
if __name__ == "__main__":
    unittest.main()
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())

    #run tests with python3 -m unittest test_backup.py
